Title: Dummy's Guide to Modern Samplers

URL Source: https://rentry.co/samplers

Markdown Content:
 
 
 
 
   
  
  
 
 
 
 
     
 
  
 

Dummy's Guide to Modern LLM Sampling  
 
 
Intro Knowledge
 
Short Glossary 
Why tokens?
 
Why not letters? 
Why not whole words? 
How are the sub-words chosen?   
How does the model generate text? 
From Tokens to Text: How LLMs Generate Content   
Sampling
 
Notes on Algorithm Presentations
 
Notation Guide 
Implementation Considerations   
Temperature 
Presence Penalty 
Frequency Penalty 
Repetition Penalty 
DRY (Don't Repeat Yourself) 
Top-K 
Top-P 
Min-P 
Top-A 
XTC (eXclude Top Choices) 
Top-N-Sigma 
Tail-Free Sampling 
Eta Cutoff 
Epsilon Cutoff 
Locally Typical Sampling 
Quadratic Sampling 
Mirostat Sampling 
Dynamic Temperature Sampling 
Beam Search 
Contrastive Search   
Sampler Order
 
The Typical Sampling Pipeline 
Effects and Interactions of Samplers with Each Other
 
How Samplers Transform Distributions 
Critical Order-Dependent Interactions
 
Temperature Before vs. After Filtering 
Penalties Before vs. After Other Samplers 
DRY's Position Matters   
Synergies and Conflicts
 
Synergistic Combos 
Conflicting Combos       
Advanced: More on Tokenizers
 
Building the Vocabulary
 
Byte Pair Encoding (BPE) 
SentencePiece 
Vocabulary Size and Granularity 
Token Boundaries and Phrasing 
Handling Rare or New Words       
Intro Knowledge  
Large Language Models (LLMs) work by taking a piece of text (e.g. user prompt) and calculating the next word. In more technical terms, tokens. LLMs have a vocabulary, or a dictionary, of valid tokens, and will reference those in training and inference (the process of generating text). More on that below. You need to understand why we use tokens (sub-words) instead of words or letters first. But first, a short glossary of some technical terms that aren't explained in the sections below in-depth: 
Short Glossary  
Logits: The raw, unnormalized scores output by the model for each token in its vocabulary. Higher logits indicate tokens the model considers more likely to come next.
 Softmax: A mathematical function that converts logits into a proper probability distribution - values between 0 and 1 that sum to 1.
 Entropy: A measure of uncertainty or randomness in a probability distribution. Higher entropy means the model is less certain about which token should come next.
 Perplexity: Related to entropy, perplexity measures how "surprised" the model is by the text. Lower perplexity indicates higher confidence.
 n-gram: A contiguous sequence of n tokens. For example, "once upon a" is a 3-gram.
 Context window (or sequence length): The maximum number of tokens an LLM can process at once, including both the prompt and generated output.
 Probability distribution: A function that assigns probabilities to all possible outcomes (tokens) such that they sum to 1. Think of it like percentages: if 1% was 0.01, 50% was 0.5, and 100% was 1.0. 
Why tokens?  
Your first instinct might be using a vocabulary of words or letters for an LLM. But instead, we use sub-words: some common words are preserved as whole in the vocabulary (e.g. the, or apple might be a single token due to how common they are in the English language), but others are fragmented into common sub-words (e.g. bi-fur-cat-ion Why is this? There are several, very good reasons: 
Why not letters?  
Many reasons. To name a few: LLMs have a limited context window (amount of tokens it can process at once). With character-level tokenization, even a moderate amount of text would lead to sequence length explosion (too many tokens for too little text). The word tokenization would be 12 tokens instead of, for example, 2 or 3 in a sub-word system. Longer sequences also require much more computation for self-attention. But more importantly, the model would need to learn higher-level patterns spanning a lot more positions. Understanding that t-h-e represents a single concept requires connecting information across three positions instead of one. This may also lead to meaningful relationships becoming more distant. Related concepts might be dozens or hundreds of positions apart. 
Why not whole words?  
A pure world-level tokenization would need us to create a vocabulary spanning the entire possible word list in the English language, and if we're doing multiple languages, then many times that. This would make our embedding matrix unreasonably large and expensive. It would also struggle with new or rare words. When a model encounters a word not in its vocabulary, it typically replaces it with an "unknown" token, losing virtually all semantic information. Sub-word tokenization would represent new words by combining existing subword tokens. For example, if we invent a new word called "grompuficious", a sub-word tokenizer might represent it as g-romp-u-ficious, depending on the tokenizer. 
 Another thing to mention is morphological awareness: many languages create words by combining morphemes (prefixes, roots, suffixes). E.g., as demonstrated earlier, unhappiness can be broken into un-happi-ness; sub-word tokenization can naturally capture these relationships. It also allows us to perform cross-lingual transfer. For languages with complex morphology or compounding (e.g. German or Finnish where words can be extremely long combinations).  
How are the sub-words chosen?  
If a language model uses a new tokenizer, the development team may decide to take a representative sample of their training data, and train a tokenizer to find the most commond sub-words in the dataset. They will set a vocabulary size beforehand, and then the tokenizer will try and find enough sub-words to fill up the list. 
How does the model generate text?  
During training, the model sees many terabytes worth of text and builds an internal probability map for tokens. For example, after it's seen the tokens for How are are usually followed by the tokens you?, it will learn that to be the most probable next set of tokens. Once this map has been built internally to a satisfactory degree, the training is stopped and a checkpoint is released to the public (or kept private and served from an API, e.g. OpenAI). During inference, the user will provide the LLM with a text, and the LLM, based on the probabilities it's learned through training, will decide what token comes next. However, it will not decide just one token: it will take into consideration every possible token that exists in its vocabulary, assigns a probability score to each, and (depending on your sampler) will only output the most probable token, i.e. the one with the highest score. This would make for a rather boring output (unless you need determinism), so this is where Sampling comes in. 
From Tokens to Text: How LLMs Generate Content  
Now that we understand how LLMs break down and represent text using tokens, let's explore how they actually generate content. The process of text generation in LLMs involve two key steps: 
 
Prediction: For each position, the model calculates the probability distribution over all possible next tokens in its vocabulary. 
Selection: The model must choose one token from this distribution to add to the growing text.  
The first step is fixed - determined by the model's parameters after training. However, the second step - token selection - is where sampling occurs. While we could simply always choose the most likely token (known as "greedy" sampling), this tends to produce repetitive, deterministic text. Sampling introduces controlled randomness to make outputs more varied. 
Sampling  
As explained above, LLMs will pick the most probable token to generate. Sampling is the practice of introducing controlled randomness. With pure "greedy" sampling, it would pick the #1 option every time, but that's boring! We use sampling methods like temperature, penalties, or truncation to allow for a bit of creative variation. This document will go through every popular sampling method, and explains how all of them word; both from a simple-to-understand and technical perspectives. 
Notes on Algorithm Presentations  
Throughout this document, algorithms are presented in pseudo-code format that combines mathematical notation with programming concepts. Here are some guidelines to help interpret these: 
Notation Guide  
 
L: the logits tensor (raw scores output by the model) 
P: probabilities (after applying softmax to logits) 
←: assignment operation (equal to = in programming) 
∑: summation 
|x|: either absolute value or length/size of x, depending on context 
x[i]: accessing the i-th element of x 
v: logical OR operation 
¬: logical NOT operation 
∞: infinity (often used to mask out tokens by setting logits to negative infinity) 
argmax(x): returns the index of the maximum value in x 
∈: "element of" (e.g., x ∈ X means x is an element of set X)  
Implementation Considerations  
The algorithms provided are written for clarity rather than optimization. Production implementations would typically: 
 
Vectorize operations where possible for efficiency 
handle edge cases and numerical stability issues (though parts that need this have occasionally been highlighted in the algorithms below) 
Incorporate batch processing for multiple sequences, if necessary for the framework 
Cache intermediate results where beneficial  
Temperature  
Think of this as the "creativity knob" on your LLM. At low temperatures (close to 0), the model becomes very cautious and predictable - it almost always picks the most likely next word. It's like ordering the same dish at your favourite restaurant every time because you know you'll like it (or maybe you don't know any better). At higher temperatures (like 0.7-1.0), the model gets very creative and willing to take chances. It may choose the 3rd or 4th most likely word instead of always the top choice. This makes text more varied and interesting, but also increases the chance of errors. Very high temperatures (above 1.0) make the model wild and unpredictable, unless you use it in conjunction with other sampling methods (e.g. min-p) to reign it in. 
Technical:
 Temperature works by directly manipulating the probability distribution over the vocabulary. The model produces logits (unnormalized scores) for each token in the vocabulary, which are then divided by the temperature value. When temperature is less than 1, this makes high logits relatively higher and low logits relatively lower, giving us a more peaked distribution where the highest-scoring tokens become even more likely. When temperature exceeds 1, this flattens the distribution, making the probability gap between high and low scoring tokens smaller, thus increasing randomness. After applying temperature, the modified logits are converted to a probability distribution (using softmax) and a token is randomly sampled from this distribution. The mathematical effect is that Temperature T transformers probabilities by essentially raising each probability to the power of 1/T before renormalizing. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8
Algorithm 1 Temperature Sampling Required: Logits tensor L, temperature parameter T Output: Modified logits with adjusted probability distribution 1: if T < 0.1 then 2: L ← L - max(L) + 1 // Shift range to [-inf, 1] for numerical stability 3: end if 4: L ← L / T // Apply temperature scaling 5: return L    
Presence Penalty  
This discourages the model from repeating any token that has appeared before, regardless of how many times it's been used. Think of it like a party host who wants to make sure everyone gets a turn to speak. If Tim has already spoken once, he gets slightly discouraged from speaking again, whether he spoke once or ten times before. This is generally not recommend, since better penalty strategies exist (see: DRY). 
Technical:
 Presence Penalty works by applying a fixed penalty to any token that has appeared in the generated text. We first identify which tokens have been used before using the output mask (which is True for tokens that appear at least once). It then subtracts the presence penalty value from the logits to those tokens. This makes previously used tokens less likely to be selected again, regardless of how frequently they've appeared. The penalty is applied uniformly to any token that has been used at least once. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8
Algorithm 2 Presence Penalty Required: Logits tensor L, output tokens O, penalty weight λp Output: Modified logits with penalty applied for token presence 1: Vsize ← |L[0]| // Vocabulary size from logits dimension 2: Moutput ← BinaryMask(O, Vsize) // Create binary mask where token has appeared at least once 3: P ← λp · Moutput // Calculate penalty matrix 4: L ← L - P // Apply presence penalty to logits 5: return L    
Frequency Penalty  
Discourages tokens based on how many times they've already been used. This is simply Presence Penalty but with the number of occurrences being taken into account. The more frequently a word has appeared, the less likely it will appear again. 
Technical:
 The frequency penalty multiplies the count of each token's previous occurrences by the penalty value and subtracts this from that token's logit score. We track how many times each token has appeared in the generated output, and if it's appeared three times, its logit is reduced 3 x (frequency penalty). This creates a progressive penalty that increases with each repeated use of a token. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8
Algorithm 3 Frequency Penalty Required: Logits tensor L, output tokens O, penalty weight λf Output: Modified logits with penalty applied proportional to token frequency 1: Vsize ← |L[0]| // Vocabulary size from logits dimension 2: Coutput ← TokenCounts(O, Vsize) // Count occurrences of each token in output 3: P ← λf · Coutput // Calculate penalty matrix proportional to counts 4: L ← L - P // Apply frequency penalty to logits 5: return L    
Repetition Penalty  
The repetition penalty works a bit differently from the other two: it penalizes both tokens from the prompt and generated output, affecting positive and negative logits differently. For positive scores, it divides the score by the penalty (making it smaller); for negative scores, it multiplies by the penalty (making it more negative). Useful for breaking out of loops, with the cost of coherency at more aggressive values. 
Technical:
 The penalty is applied to tokens that have appeared in either prompt or the generated text so far. We create a mask combining both prompt and output masks. for tokens in this combined mask, we apply the penalty by either dividing or multiplying the logits depending on whether they're positive or negative. This approach avoids over-penalizing already unlikely tokens while effectively reducing the probability of tokens with higher scores. The most distinctive feature is its different treatment of positive and negative logits, which helps maintain a more balanced probability distribution. 
Algorithm
 
 
 
 
⎗ 
✓   
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
Algorithm 4 Repetition Penalty Required: Logits tensor L, prompt tokens P, output tokens O, penalty factor λr Output: Modified logits with asymmetric penalty for repeated tokens 1: Vsize ← |L[0]| // Vocabulary size from logits dimension 2: Mprompt ← BinaryMask(P, Vsize) // Create binary mask for tokens in prompt 3: Moutput ← BinaryMask(O, Vsize) // Create binary mask for tokens in output 4: M ← Mprompt ∨ Moutput // Combined mask for tokens in either prompt or output 5: R ← matrix of size |L| × Vsize filled with λr 6: R[¬M] ← 1.0 // No penalty for tokens not previously seen 7: for each position (i,j) in L do 8: if L[i,j] > 0 then 9: L[i,j] ← L[i,j] / R[i,j] // Divide positive logits 10: else 11: L[i,j] ← L[i,j] * R[i,j] // Multiply negative logits 12: end if 13: end for 14: return L    
DRY (Don't Repeat Yourself)  
DRY sampling is like having an editor who watches for repetitive patterns in your writing. Let's say you're writing a story and you've already used the phrase "once upon a time" - DRY will discourage you from using that exact same phrase again. But it's much smarter than simple word repetition prevention (like the 3 penalties above). 
DRY looks for repeating patterns (called n-grams) in your text. If it notices you've written something like "the cat sat on the" before and you're about to repeat this pattern, it discourages the next word that would continue the repetition. The longer the repeating pattern, the stronger the discouragement. This prevents the text from falling into loops or recycling the same phrases and keeps the output fresh and varied. What makes DRY special is that it considers existing patterns. It's particularly useful for creative writing where repetitive text would sound unnatural. 
Technical:
 DRY sampling works by detecting n-gram repetitions and penalizing tokens that would continue these patterns. The algorithm examines the sequence of tokens generated so far and identifies repeating patterns that end with the most recently generated token. We track where the last token appears elsewhere in the text, then compares the contexts before these appearances. When it finds matching contexts (repeated n-grams), it identifies which tokens followed these patterns previously and penalizes them in the current logits distribution. Key parameters include the multiplier (strength of the penalty), base (how much stronger the penalty becomes for longer n-grams), minimum n-gram length to consider, and maximum n-gram length to check. The algorithm also respects "sequence breakers" (like punctuation) that reset pattern matching, and has range limits to only consider recent text for efficiency. 
The penalty is applied exponentially based on the length of the matching pattern, with longer matches receiving stronger penalties. This creates a dynamic system that prevents repetition while still allowing natural text flow, making output text more diverse and human-like by avoiding the repetitive patterns that often plague language models. 
Algorithm
 
 
 
 
⎗ 
✓   
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
Algorithm 5 DRY (Don't Repeat Yourself) Sampling Required: Logits tensor L, input tokens I, output tokens O, multiplier λ, base b,  minimum n-gram length Nmin, sequence breaker tokens B, range limit r,  maximum n-gram length Nmax, maximum occurrences M, early exit threshold E Output: Modified logits with penalties for repeating patterns  1: for each sequence s where λ > 0 do 2: // Prepare token sequence by concatenating prompt and generated tokens 3: p ← Length of valid tokens in I[s] 4: q ← Length of valid tokens in O[s] 5: T ← Concatenate(I[s][1:p], O[s][1:q]) 6: 7: if r > 0 then 8: T ← T[-r:] // Consider only the last r tokens if range limit is set 9: end if 10: 11: if |T| < 2 then continue end if // Skip if sequence too short 12: 13: last ← T[-1] // Last token in sequence 14: if last ∈ B then continue end if // Skip if last token is a sequence breaker 15: 16: // Create mask for sequence breaker positions 17: breakMask ← ZeroVector(|T|) 18: for each token id b ∈ B do 19: breakMask ← breakMask ∨ (T = b) 20: end for 21: 22: // Find maximum allowed n-gram length before hitting a sequence breaker 23: maxN ← 0 24: for i from 1 to min(|breakMask|, Nmax) do 25: if breakMask[-i] then break end if 26: maxN ← i 27: end for 28: 29: if maxN ≤ Nmin then continue end if // Skip if maximum n-gram too short 30: 31: // Initialize array to track longest matching n-gram for each token 32: ngramLengths ← ZeroVector(VocabularySize) 33: 34: // Find all positions where the last token appears 35: endpoints ← FindIndices(T = last) 36: if |endpoints| < 2 then continue end if 37: 38: // Remove the last occurrence (current position) 39: endpoints ← endpoints[:-1] 40: 41: // Limit number of previous occurrences to check 42: if |endpoints| > M then 43: endpoints ← endpoints[-M:] 44: end if 45: 46: // Check each previous occurrence of the last token for matching contexts 47: for each idx in Reverse(endpoints) do 48: if idx = |T| - 1 then continue end if 49: 50: matchLen ← 0 51: // Look backward to find matching context 52: for u from 1 to min(idx, maxN) do 53: if breakMask[idx - u] then break end if 54: if T[idx - u] ≠ T[-u - 1] then break end if 55: matchLen ← u 56: end for 57: 58: if matchLen > 0 then 59: nextToken ← T[idx + 1] // Token that followed this pattern before 60: newLen ← matchLen + 1 61: ngramLengths[nextToken] ← max(ngramLengths[nextToken], newLen) 62: 63: if newLen ≥ E then break end if // Early exit if match is long enough 64: end if 65: end for 66: 67: // Apply penalties to tokens that would continue repeating patterns 68: penaltyMask ← (ngramLengths > 0) 69: if any(penaltyMask) then 70: scales ← b ^ (ngramLengths[penaltyMask] - Nmin) // Exponential scaling by pattern length 71: L[s][penaltyMask] ← L[s][penaltyMask] - λ * scales 72: end if 73: end for 74: return L    
Top-K  
Instead of considering all possible next words (which could be tens of thousands), the model narrows down to only the K most likely candidates. If K is 40, the model will only choose from the top 40 most likely next words. This approach prevents the model from selecting extremely unlikely words while still maintaining some randomness. 
Technical:
 This method works by sorting the logits for all possible next tokens and keeping only the K highest values while setting all others to negative infinity. We first sort the logits in ascending order and get their indices. Then, we identify the Kth highest value and create a mask for all values below this threshold. Any logit below this threshold is set to -inf, ensuring these tokens have effectively zero probability after applying softmax. The filtered logits are then returned to their original order using the saved indices. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8 9
Algorithm 6 Top-K Sampling Required: Logits tensor L, parameter k Output: Modified logits with all but top-k options filtered out 1: Lsorted, Lidx ← Sort(L, descending=False) // Sort logits in ascending order 2: kth ← Lsorted[|Lsorted| - k] // Find the kth largest logit value 3: mask ← Lsorted < kth // Create mask for values below the threshold 4: Lsorted[mask] ← -∞ // Filter out tokens below threshold 5: L ← Unsort(Lsorted, Lidx) // Restore original ordering 6: return L    
Top-P  
Instead of picking a fixed number of options like Top-K, Top-P selects the smallest set of words whose combined probability exceeds threshold P. It's like saying "I'll only consider dishes that make up 90% of all orders at this restaurant." If P is 0.9, the model includes just enough of the highest-probability words to reach 90% cumulative probability, whether that's 5 words or 500. In situations where the model is very confident, it might only need a few options, but when uncertainty is high, it can consider more possibilities. 
Technical:
 Top-P works by selecting the smallest set of tokens whose cumulative probability exceeds the threshold P. After applying Top-K filtering, we convert logits to probabilities using softmax and calculates their cumulative sum in ascending order. It then creates a mask identifying tokens where the cumulative probability is still below 1-P (i.e. these tokens aren't part of the "nucleus" that makes up P of the total probability mass). These tokens are masked out by setting their logits to -inf. We need to ensure that at least one token remains viable by always keeping the highest-probability token (setting its mask to False). Finally, the filtered logits are returned to their original order using the saved indices from the initial sorting. 
Algorithm
 
 
 
 
⎗ 
✓   
 1  2  3  4  5  6  7  8  9 10 11
Algorithm 7 Top-P (Nucleus) Sampling Required: Logits tensor L, probability threshold p ∈ [0,1] Output: Modified logits with smallest probability tokens filtered out 1: Lsorted, Lidx ← Sort(L, descending=False) // Sort logits in ascending order 2: Psorted ← Softmax(Lsorted) // Convert to probabilities 3: Pcum ← CumulativeSum(Psorted) // Calculate cumulative probabilities 4: mask ← Pcum ≤ (1 - p) // Create mask for tokens below threshold 5: mask[|mask| - 1] ← False // Always keep at least one token 6: Lsorted[mask] ← -∞ // Filter out tokens below threshold 7: L ← Unsort(Lsorted, Lidx) // Restore original ordering 8: return L    
Min-P  
Min-P sets a quality threshold relative to these best option. Using the restaurant analogy again, imagine you're at a restaurant with your friend who always orders the most popular dish. You decide you'll only consider dishes that are at least 20% as popular as their top choice. If the most popular dish gets ordered 100 times a day, you set Min-P to 0.2, you'll only consider dishes ordered at least 20 times a day. When the model is very confident about the best choice, the threshold becomes higher, and fewer alternatives are considered. When the model is uncertain, more alternatives pass the threshold. 
Min-P is usually used in conjunction with higher temperature values (1.0-1.2), and used in very low values (0.1). 
Technical:
 Min-P filters out tokens whose probabilities fall below a certain fraction of the highest probability token. We first convert logits to probabilities using softmax and identify the maximum probability value for each sequence. Then, create a threshold by multiplying this maximum probability by the Min-P value. For example, if the highest probability is 0.6 and Min-P is 0.1, the threshold would be 0.06. 
Any token with a probability below this threshold is masked out by setting its logit to -inf. This creates a dynamic filtering mechanism where the cutoff adapts to the confidence level of the model for each prediction. Min-P doesn't require sorting the entire vocabulary like Top-K or Top-P, so it ends up being more efficient as well. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8 9
Algorithm 8 Min-P Sampling Required: Logits tensor L, threshold fraction min_p ∈ [0,1] Output: Modified logits with low probability tokens filtered out 1: P ← Softmax(L) // Convert logits to probabilities 2: Pmax ← Max(P) // Find maximum probability 3: threshold ← min_p × Pmax // Calculate dynamic threshold 4: mask ← P < threshold // Create mask for tokens below threshold 5: L[mask] ← -∞ // Filter out tokens below threshold 6: return L    
Top-A  
This one applies a filter that gets stricter when the model is more confident. Top-A creates a threshold that's proportional to the square of the highest probability token. When the model is very confident, the threshold becomes much higher due to the squaring effect, dramatically limiting options only to the very best alternatives. When the model is less confident, the threshold drops more rapidly. 
Technical: 
Top-A is essentially if min-p was squared instead of linear. Note that Top-A predates Min-P. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8 9
Algorithm 9 Top-A Sampling Required: Logits tensor L, parameter a Output: Modified logits with options below squared threshold filtered out 1: P ← Softmax(L) // Convert logits to probabilities 2: Pmax ← Max(P) // Find maximum probability 3: threshold ← Pmax² × a // Calculate squared threshold 4: mask ← P < threshold // Create mask for tokens below threshold 5: L[mask] ← -∞ // Filter out tokens below threshold 6: return L    
XTC (eXclude Top Choices)  
XTC works by occasionally excluding the most likely option based on two parameters: a probability of activation, and a threshold for determining which choices to exclude. When XTC activates (based on random chance), it looks at all the top choices whose probabilities exceed the threshold and removes all but the lowest-scoring one among them. 
This forces the model to occasionally "think outside the box" and select words it wouldn't normally. Unlike other samplers that just filter out unlikely options, XTC specifically targets the most predictable choices. 
Technical:
 XTC occasionally excludes the most likely token from consideration, keeping only the least likely token among those that exceed a specified threshold. We first determine whether to apply XTC for each sequence based on a random draw against the specified probability. For sequences where XTC activates, we convert logits to probs, sort them in descending order, and identify tokens whose probabilities exceed the threshold (skipping the very top choices initially). If tokens above the threshold are found, we count how many tokens qualify (including the top choice that was initially skipped). We then mask out all these high-prob tokens except for the last/lowest one in the sorted list. This effectively removes the most obvious choices. You can call this sampler a contrarian. 
Algorithm
 
 
 
 
⎗ 
✓   
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Algorithm 10 XTC (eXclude Top Choices) Sampling Required: Logits tensor L, threshold t, activation probability p Output: Modified logits with top choices filtered out except for the lowest-scoring one 1: apply ← RandomBernoulli(p) // Determine which sequences to apply XTC to 2: if not any(apply) then return L end if 3: 4: P ← Softmax(L) // Convert logits to probabilities 5: Psorted, Pidx ← Sort(P, descending=True) // Sort probabilities in descending order 6: 7: for each sequence i where apply[i] = True do 8: // Find tokens above threshold (starting from second-highest) 9: aboveThreshold ← Psorted[i, 1:] ≥ t 10: 11: // Count how many tokens qualify (including the top one) 12: count ← Sum(aboveThreshold) + 1 13: 14: if count > 1 then 15: // Get indices of the high-probability tokens to remove 16: tokensToRemove ← Pidx[i, 0:count-1] 17: 18: // Mask out all high-probability tokens except the lowest-scoring one 19: L[i, tokensToRemove] ← -∞ 20: end if 21: end for 22: 23: return L    
Top-N-Sigma  
This one sets a statistical quality bar for word choices. Think of it like selecting players for a sports team and decide to take anyone who scores within 2 standard deviations of the top performer. 
The sampler uses basic statistics to create a more adaptive threshold. It looks at how spread out (standard deviation) the scores for all possible next words are, then sets a cutoff at N standard deviations below the highest-scoring word. In situations where the model has a few very strong preferences and many mediocre options, the standard deviation will be small, creating a stricter threshold. But when there are many similarly good options, the standard deviation increases. Essentially, when the model is certain about a few good choices, it stays focused on those. When there are multiple reasonable options (like in creative writing), it allows for more variety without including truly poor choices. 
Technical:
 Top-N-Sigma creates a threshold based on statistical properties of the distribution of logits, specifically the maximum value and standard deviation. We calculate the standard deviation of logits across the vocabulary for each sequence. Then, set a threshold by subtracting N times this standard deviation from the maximum logit value. any logit below this threshold is set to -inf. The approach is mathematically elegant because it adapts to the shape of the distribution rather than just its absolute values. In distributions with high variance, the threshold will be lower, allowing more tokens in. It accounts for both the absolute best score and the overall distribution of scores. 
Algorithm
 
 
 
 
⎗ 
✓   
1 2 3 4 5 6 7 8 9
Algorithm 11 Top-N-Sigma Sampling Required: Logits tensor L, parameter n (number of standard deviations) Output: Modified logits with values below statistical threshold filtered out 1: σ ← StandardDeviation(L) // Calculate standard deviation of logits across vocabulary 2: Lmax ← Max(L) // Find maximum logit value 3: threshold ← Lmax - n × σ // Calculate threshold n standard deviations below maximum 4: mask ← L < threshold // Create mask for tokens below threshold 5: L[mask] ← -∞ // Filter out tokens below threshold 6: return L    
Tail-Free Sampling  
TFS is like looking at the slope change in a graph of word probabilities and cutting it off where there's a significant drop. For example, you're lining up candidates for a job based on their scores - instead of using a fixed cutoff, you look for where there's a big gap between consecutive scores and say "everyone past this point is significantly worse." 
TFS examines how the probability distribution changes by looking at second derivatives (the "curvature" or rate of change in the slope). It focues on points where the distribution