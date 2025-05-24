import requests
import json
import os
import logging
import time
from functools import wraps
# from urllib.parse import quote # No longer used here, moved to core_logic.py
from waybackpy import WaybackMachineSaveAPI

# -- configurations begin --
MAX_CONTENT_LENGTH: int = 32 * 1024  # 32KB
# -- configurations end --

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Entering {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'Exiting {func.__name__} - Elapsed time: {elapsed_time:.4f} seconds')
        return result
    return wrapper

@log_execution_time
def submit_to_wayback_machine(url: str):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    try:
        save_api = WaybackMachineSaveAPI(url, user_agent)
        wayback_url = save_api.save()
        logging.info(f'Wayback Saved: {wayback_url}')
    except Exception as e:
        # 非关键路径，容忍失败
        logging.warning(f"submit to wayback machine failed, skipping, url={url}")
        logging.exception(e)

@log_execution_time
def get_text_content(url: str) -> str:
    jina_url: str = f"https://r.jina.ai/{url}"
    response: requests.Response = requests.get(jina_url)
    content = response.text
    if len(content) > MAX_CONTENT_LENGTH:
        logging.warning(f"Content length ({len(content)}) exceeds maximum ({MAX_CONTENT_LENGTH}), truncating...")
        content = content[:MAX_CONTENT_LENGTH]
    return content

@log_execution_time
def call_openai_api(prompt: str, content: str) -> str:
    model: str = os.environ.get('OPENAI_API_MODEL', 'gpt-4o-mini')
    headers: dict = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json"
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    }
    api_endpoint: str = os.environ.get('OPENAI_API_ENDPOINT', 'https://api.openai.com/v1/chat/completions')
    
    # 添加请求相关日志
    logging.info(f"Calling OpenAI API with model: {model}")
    logging.info(f"API endpoint: {api_endpoint}")
    
    response: requests.Response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    
    # 添加响应相关日志
    logging.info(f"Response status code: {response.status_code}")
    response_json = response.json()
    logging.debug(f"Response content: {json.dumps(response_json, ensure_ascii=False)}")
    
    # 错误处理
    if response.status_code != 200:
        error_msg = f"OpenAI API request failed with status {response.status_code}"
        logging.error(error_msg)
        logging.error(f"Error response: {response_json}")
        raise Exception(error_msg)
    
    if 'choices' not in response_json:
        error_msg = "Response does not contain 'choices' field"
        logging.error(error_msg)
        logging.error(f"Full response: {response_json}")
        raise Exception(error_msg)
        
    return response_json['choices'][0]['message']['content']
