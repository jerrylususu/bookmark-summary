Title: 6 Techniques I Use to Create a Great User Experience for Shell Scripts

URL Source: https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts

Published Time: 2024-09-11T00:00:00.000Z

Markdown Content:
> "You should go and check out the shell script in the repo because it's very nice. It has colored output, it's super safe... it's really a masterclass in terms of writing shell scripts."

Thank you Gunnar Morling for the shout-out! 😊

In January 2024, I along with a few dozen performance-minded geeks got nerd-sniped into participating in Gunnar's One Billion Row Challenge 1️⃣🐝🏎️ .

Gunnar quickly became overwhelmed being the (unpaid) evaluator of a constant stampede of entries. I jumped in to help him automate the evaluation steps with a shell script and received the above testimonial from Gunnar at his Javazone talk (check it out to hear all about the performance techniques used in the challenge: ["# 1BRC–Nerd Sniping the Java Community - Gunnar Morling"](https://vimeo.com/1006554858)).

Here are 6 techniques I used in the #1BRC shell script to make it robust, safe and fun for Gunnar to use:

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#1.-comprehensive-error-handling-and-input-validation)1\. Comprehensive Error Handling and Input Validation
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I believe that clear error messages are crucial for a good user experience. That's why I implemented thorough error handling and input validation throughout the script. For example:

```
if [ -z "$1" ] 
  then 
    echo "Usage: evaluate.sh <fork name> (<fork name 2> ...)" 
    echo " for each fork, there must be a 'calculate_average_<fork name>.sh' script and an optional 'prepare_<fork name>.sh'." 
    exit 1 
fi
```

This approach helps users quickly identify and resolve issues, saving them time and frustration.

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#2.-clear-and-colorful-output)2\. Clear and Colorful Output
-------------------------------------------------------------------------------------------------------------------------------------------------------------

To make the script's output more readable and user-friendly, I used ANSI color codes to highlight important information, warnings, and errors. For instance:

```
BOLD_RED='\033[1;31m'
RESET='\033[0m'
echo -e "${BOLD_RED}ERROR${RESET}: ./calculate_average_$fork.sh does not exist." >&2
```

This visual distinction helps users quickly grasp the nature of each message.

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#3.-detailed-progress-reporting)3\. Detailed Progress Reporting
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

I wanted users to understand exactly what the script was doing at each step. To achieve this, I implemented a function that prints each command before executing it:

```
function print_and_execute() {
  echo "+ $@" >&2 
  "$@" 
}
```

This matches the output format of Bash's builtin `set -x` tracing, but gives the script author more granular control of what is printed.

This level of transparency not only keeps users informed but also aids in debugging if something goes wrong.

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#4.-strategic-error-handling-with-%22set-e%22-and-%22set-+e%22)4\. Strategic Error Handling with "set -e" and "set +e"
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I wanted to ensure that the script would exit immediately if there was an error in the script itself, but also allow it to continue running if individual forks encountered issues. To achieve this, I used the Bash options "set -e" and "set +e" strategically throughout the script. Here's how I implemented this technique:

```
# At the beginning of the script
set -eo pipefail

# Before running tests and benchmarks for each fork
for fork in "$@"; do
  set +e # we don't want prepare.sh, test.sh or hyperfine failing on 1 fork to exit the script early

  # Run prepare script (simplified)
  print_and_execute source "./prepare_$fork.sh"

  # Run the test suite (simplified)
  print_and_execute $TIMEOUT ./test.sh $fork

  # ... (other fork-specific operations)
done
set -e  # Re-enable exit on error after the fork-specific operations
```

This approach gives the script author fine-grained control over which errors cause the script to exit and which can be handled in other ways.

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#5.-platform-specific-adaptations)5\. Platform-Specific Adaptations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Knowing that users might run this script on different operating systems, I added logic to detect the OS and adjust the script's behavior accordingly:

```
if [ "$(uname -s)" == "Linux" ]; then 
  TIMEOUT="timeout -v $RUN_TIME_LIMIT" 
else # Assume MacOS 
  if [ -x "$(command -v gtimeout)" ]; then 
    TIMEOUT="gtimeout -v $RUN_TIME_LIMIT"
  else 
    echo -e "${BOLD_YELLOW}WARNING${RESET} gtimeout not available, install with `brew install coreutils` or benchmark runs may take indefinitely long." 
  fi
fi
```

This ensures a consistent experience across different environments. Many #1BRC participants were developing on MacOS while the evaluation machine ran linux for example.

[](https://nochlin.com/blog/6-techniques-i-use-to-create-a-great-user-experience-for-shell-scripts#6.-timestamped-file-outputs-for-multiple-runs)6\. Timestamped File Outputs for Multiple Runs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support multiple benchmark runs without overwriting previous results, I implemented a system of timestamped file outputs. This allows users to run the script multiple times and keep a historical record of all results. Here's how I did it:

```
filetimestamp=$(date +"%Y%m%d%H%M%S")

# ... (in the loop for each fork)
HYPERFINE_OPTS="--warmup 0 --runs $RUNS --export-json $fork-$filetimestamp-timing.json --output ./$fork-$filetimestamp.out"

# ... (after the benchmarks)
echo "Raw results saved to file(s):"
for fork in "$@"; do
  if [ -f "$fork-$filetimestamp-timing.json" ]; then
      cat $fork-$filetimestamp-timing.json >> $fork-$filetimestamp.out
      rm $fork-$filetimestamp-timing.json
  fi

  if [ -f "$fork-$filetimestamp.out" ]; then
    echo "  $fork-$filetimestamp.out"
  fi
done
```

\--

Check out the complete benchmark evaluation script in the #1BRC repo: [evaluate.sh](https://github.com/gunnarmorling/1brc/blob/main/evaluate.sh)

By implementing these techniques, I aimed to create a user-friendly, informative, and robust shell script that provides a great experience for users running and analyzing benchmarks. I hope these ideas inspire you to enhance the user experience in your own shell scripts!

I'd love to hear your thoughts on these shell scripting techniques or any other tips you have for creating great user experiences in scripts. Feel free to join the discussion:

*   On Hacker News: [Discuss this post on Hacker News](https://news.ycombinator.com/item?id=41512899)
*   On Twitter: [Share your thoughts on Twitter](https://x.com/jasonnochlin/status/1833903787251318798)
