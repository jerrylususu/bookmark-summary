Title: A Visual Guide to Quantization

URL Source: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization

Published Time: 2024-07-22T14:38:38+00:00

Markdown Content:
##### Translations _\- [Korean](https://tulip-phalange-a1e.notion.site/a947f0efb8eb4813a533b0d957134f6d)_

As their name suggests, Large Language Models (LLMs) are often too large to run on consumer hardware. These models may exceed billions of parameters and generally need GPUs with large amounts of VRAM to speed up inference.

As such, more and more research has been focused on making these models smaller through improved training, adapters, etc. One major technique in this field is called _quantization_.

[![Image 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9d17077-d9af-4b37-9b9b-57ef9aaa1ca9_680x486.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9d17077-d9af-4b37-9b9b-57ef9aaa1ca9_680x486.png)

In this post, I will introduce the field of quantization in the context of language modeling and explore concepts one by one to develop an intuition about the field. We will explore various methodologies, use cases, and the principles behind quantization.

As a visual guide, expect many visualizations to develop an intuition about quantization!

##### **Table of Contents**

*   _**Part 1: The “Problem” with Large Language Models**_
    
    *   [How to Represent Numerical Values](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7how-to-represent-numerical-values)
        
    *   [Memory Constraints](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7memory-constraints)
        
*   _**Part 2: Introduction to Quantization**_
    
    *   [Common Data Types](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7common-data-types)
        
        *   [FP16](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7fp16)
            
        *   [BF16](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7bf16)
            
        *   [INT8](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7int8)
            
    *   [Symmetric Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7symmetric-quantization)
        
    *   [Asymmetric Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7asymmetric-quantization)
        
    *   [Range Mapping and Clipping](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7range-mapping-and-clipping)
        
    *   [Calibration](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7calibration)
        
        *   [Weights (and Biases)](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7weights-and-biases)
            
        *   [Activations](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7activations)
            
*   _**Part 3: Post-Training Quantization (PTQ)**_
    
    *   [Dynamic Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7dynamic-quantization)
        
    *   [Static Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7static-quantization)
        
    *   [The Realm of 4-bit Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7the-realm-of-bit-quantization)
        
        *   [GPTQ](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7gptq)
            
        *   [GGUF](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7gguf)
            
*   _**Part 4: Quantization-Aware Training (QAT)**_
    
    *   [The Era of 1-bit LLMs: BitNet](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7the-era-of-bit-llms-bitnet)
        
        *   [Weight Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7weight-quantization)
            
        *   [Activation Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7activation-quantization)
            
        *   [Dequantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7dequantization)
            
    *   [All Large Language Models are in 1.58 Bits](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7all-large-language-models-are-in-bits)
        
        *   [The Power of 0](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7the-power-of)
            
        *   [Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#%C2%A7quantization)
            

LLMs get their name due to the number of parameters they contain. Nowadays, these models typically have billions of parameters (mostly _weights_) which can be quite expensive to store.

During inference, activations are created as a product of the input and the weights, which similarly can be quite large.

[![Image 2](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99fe2ba-d4f4-4046-850c-e3f469add123_1368x708.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99fe2ba-d4f4-4046-850c-e3f469add123_1368x708.png)

As a result, we would like to represent billions of values as efficiently as possible, minimizing the amount of space we need to store a given value.

Let’s start from the beginning and explore how numerical values are represented in the first place before optimizing them.

A given value is often represented as a floating point number (or _floats_ in computer science): a positive or negative number with a decimal point.

These values are represented by “_bits_”, or binary digits. The [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) standard describes how bits can represent one of three functions to represent the value: the _sign_, _exponent_, or _fraction (_or mantissa_)_.

[![Image 3](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8362c0e-0a77-4eda-80a8-8e5e1df4433f_1252x308.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8362c0e-0a77-4eda-80a8-8e5e1df4433f_1252x308.png)

Together, these three aspects can be used to calculate a value given a certain set of bit values:

[![Image 4](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4783fd02-a138-40c7-82c7-79dd05a179e4_1472x772.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4783fd02-a138-40c7-82c7-79dd05a179e4_1472x772.png)

The more bits we use to represent a value, the more precise it generally is:

[![Image 5](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1eafac2a-d027-4d66-95de-7030e0392b39_1796x940.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1eafac2a-d027-4d66-95de-7030e0392b39_1796x940.png)

The more bits we have available, the larger the range of values that can be represented.

[![Image 6](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff306b7f1-dd3c-4001-91d3-bd61f22c5782_1128x452.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff306b7f1-dd3c-4001-91d3-bd61f22c5782_1128x452.png)

The interval of representable numbers a given representation can take is called the _dynamic range_ whereas the distance between two neighboring values is called _precision_.

[![Image 7](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dbb8398-9f3f-4d9a-b63f-591cb37bdbdd_1144x856.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dbb8398-9f3f-4d9a-b63f-591cb37bdbdd_1144x856.png)

A nifty feature of these bits is that we can calculate how much memory your device needs to store a given value. Since there are 8 bits in a byte of memory, we can create a basic formula for most forms of floating point representation.

[![Image 8](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe146740d-72e9-44dc-99e1-f7bc42737cec_1128x144.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe146740d-72e9-44dc-99e1-f7bc42737cec_1128x144.png)

**NOTE**: In practice, more things relate to the amount of (V)RAM you need during inference, like the context size and architecture.

Now let’s assume that we have a model with 70 billion parameters. Most models are natively represented with float 32-bit (often called _full-precision_), which would require **280GB** of memory just to load the model.

[![Image 9](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c28e9b0-c002-4a49-9441-af24f261df40_1128x548.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c28e9b0-c002-4a49-9441-af24f261df40_1128x548.png)

As such, it is very compelling to minimize the number of bits to represent the parameters of your model (as well as during training!). However, as the precision decreases the accuracy of the models generally does as well.

We want to reduce the number of bits representing values while maintaining accuracy… This is where _quantization_ comes in!

Quantization aims to reduce the precision of a model’s parameter from higher bit-widths (like 32-bit floating point) to lower bit-widths (like 8-bit integers).

[![Image 10](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82ac8f88-0cf5-4244-ba9f-cbffdb283947_1008x496.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82ac8f88-0cf5-4244-ba9f-cbffdb283947_1008x496.png)

There is often some loss of precision (granularity) when reducing the number of bits to represent the original parameters.

To illustrate this effect, we can take any image and use only 8 colors to represent it:

Notice how the zoomed-in part seems more “grainy” than the original since we can use fewer colors to represent it.

The main goal of quantization is to reduce the number of bits (colors) needed to represent the original parameters while preserving the precision of the original parameters as best as possible.

First, let’s look at common data types and the impact of using them rather than 32-bit (called _full-precision_ or _FP32_) representations.

Let’s look at an example of going from 32-bit to 16-bit (called _half precision_ or _FP16_) floating point:

[![Image 11](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4ac888a-02b9-4153-915a-e103a12c33a4_1460x892.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4ac888a-02b9-4153-915a-e103a12c33a4_1460x892.png)

Notice how the range of values FP16 can take is quite a bit smaller than FP32.

To get a similar range of values as the original FP32, _bfloat 16_ was introduced as a type of “truncated FP32”:

[![Image 12](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F172c93aa-58ae-4d11-8cb7-2917c265cb68_1460x936.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F172c93aa-58ae-4d11-8cb7-2917c265cb68_1460x936.png)

BF16 uses the same amount of bits as FP16 but can take a wider range of values and is often used in deep learning applications.

When we reduce the number of bits even further, we approach the realm of _integer-based representations_ rather than floating-point representations. To illustrate, going FP32 to INT8, which has only 8 bits, results in a fourth of the original number of bits:

[![Image 13](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa37a58d-1f5a-433c-b235-5b073596bbca_1460x848.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa37a58d-1f5a-433c-b235-5b073596bbca_1460x848.png)

Depending on the hardware, integer-based calculations might be faster than floating-point calculations but this isn’t always the case. However, computations are generally faster when using fewer bits.

For each reduction in bits, a mapping is performed to “squeeze” the initial FP32 representations into lower bits.

In practice, we do not need to map the entire FP32 range \[-3.4e38, 3.4e38\] into INT8. We merely need to find a way to map the range of our data (the model’s parameters) into IN8.

Common squeezing/mapping methods are _symmetric_ and _asymmetric_ quantization and are forms of _linear mapping_.

Let’s explore these methods to quantize from FP32 to INT8.

In symmetric quantization, the range of the original floating-point values is mapped to a symmetric range around zero in the quantized space. In the previous examples, notice how the ranges before and after quantization remain centered around zero.

This means that the quantized value for zero in the floating-point space is exactly zero in the quantized space.

[![Image 14](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F730bbb8a-3a44-47f6-aefe-f652b117ae22_1124x600.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F730bbb8a-3a44-47f6-aefe-f652b117ae22_1124x600.png)

A nice example of a form of symmetric quantization is called absolute maximum (_absmax_) quantization.

Given a list of values, we take the _highest_ absolute value (**α**) as the range to perform the linear mapping.

[![Image 15](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F782beaa8-340f-45b8-ba7f-20491f66867a_1172x848.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F782beaa8-340f-45b8-ba7f-20491f66867a_1172x848.png)

Note the \[-127, 127\] range of values represents the restricted range. The unrestricted range is \[-128, 127\] and depends on the quantization method.

Since it is a linear mapping centered around zero, the formula is straightforward.

We first calculate a scale factor (_**s**_) using:

*   _**b**_ is the number of bytes that we want to quantize to (8),
    
*   **α** is the _highest_ absolute value,
    

Then, we use the _**s**_ to quantize the input _**x**_:

[![Image 16](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc76e35-13bf-4d6f-94bf-dbe4725c084f_1644x486.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cc76e35-13bf-4d6f-94bf-dbe4725c084f_1644x486.png)

Filling in the values would then give us the following:

[![Image 17](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fd92531-447c-45de-af37-f33ffc446b0b_1644x486.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fd92531-447c-45de-af37-f33ffc446b0b_1644x486.png)

To retrieve the original FP32 values, we can use the previously calculated _scaling factor_ (_**s**_) to _dequantize_ the quantized values.

[![Image 18](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe708f283-3c74-4344-ae76-e96412098c0b_1644x246.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe708f283-3c74-4344-ae76-e96412098c0b_1644x246.png)

Applying the quantization and then dequantization process to retrieve the original looks as follows:

[![Image 19](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea2d627-efc7-4a8a-9cf0-7a7020f1253d_1236x348.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea2d627-efc7-4a8a-9cf0-7a7020f1253d_1236x348.png)

You can see certain values, such as **3.08** and **3.02** being assigned to the INT8, namely **36**. When you dequantize the values to return to FP32, they lose some precision and are not distinguishable anymore.

This is often referred to as the _quantization error_ which we can calculate by finding the difference between the original and dequantized values.

[![Image 20](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe173b13b-ed99-4de0-a5e0-4b9114899b3f_1236x372.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe173b13b-ed99-4de0-a5e0-4b9114899b3f_1236x372.png)

Generally, the lower the number of bits, the more quantization error we tend to have.

Asymmetric quantization, in contrast, is not symmetric around zero. Instead, it maps the minimum (**β**) and maximum (**α**) values from the float range to the minimum and maximum values of the quantized range.

The method we are going to explore is called _zero-point quantization_.

[![Image 21](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ffa0c54-88bf-45c1-8636-bdb097bb8e6b_1172x848.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ffa0c54-88bf-45c1-8636-bdb097bb8e6b_1172x848.png)

Notice how the 0 has shifted positions? That’s why it’s called _asymmetric quantization_. The min/max values have different distances to 0 in the range \[-7.59, 10.8\].

Due to its shifted position, we have to calculate the zero-point for the INT8 range to perform the linear mapping. As before, we also have to calculate a _scale factor_ (_**s**_) but use the difference of INT8’s range instead \[-128, 127\]

[![Image 22](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16cde2f6-aeb5-44d8-b056-846a5f1a0448_1096x508.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16cde2f6-aeb5-44d8-b056-846a5f1a0448_1096x508.png)

Notice how this is a bit more involved due to the need to calculate the _zeropoint_ (_**z**_) in the INT8 range to shift the weights.

As before, let’s fill in the formula:

[![Image 23](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ad0583-277f-4168-bbc7-a5503b5e45c4_1096x468.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ad0583-277f-4168-bbc7-a5503b5e45c4_1096x468.png)

To dequantize the quantized from INT8 back to FP32, we will need to use the previously calculated _scale factor_ (_**s**_) and _zeropoint_ (_**z**_).

Other than that, dequantization is straightforward:

[![Image 24](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aee7fd2-c070-4710-9d8c-ccf598d5befe_1016x160.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aee7fd2-c070-4710-9d8c-ccf598d5befe_1016x160.png)

When we put symmetric and asymmetric quantization side-by-side, we can quickly see the difference between methods:

[![Image 25](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01404566-e2ae-4e3f-9101-cafc68d92b40_1172x716.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01404566-e2ae-4e3f-9101-cafc68d92b40_1172x716.png)

Note the zero-centered nature of symmetric quantization versus the offset of asymmetric quantization.

In our previous examples, we explored how the range of values in a given vector could be mapped to a lower-bit representation. Although this allows for the full range of vector values to be mapped, it comes with a major downside, namely _outliers_.

Imagine that you have a vector with the following values:

[![Image 26](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce7fd7ab-3c4b-401d-893e-d417db946fd8_1172x184.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce7fd7ab-3c4b-401d-893e-d417db946fd8_1172x184.png)

Note how one value is much larger than all others and could be considered an outlier. If we were to map the full range of this vector, all small values would get mapped to the same lower-bit representation and lose their differentiating factor:

[![Image 27](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72052ddb-1c54-45b3-9800-2c4335cc9581_1120x564.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72052ddb-1c54-45b3-9800-2c4335cc9581_1120x564.png)

This is the absmax method we used earlier. Note that the same behavior happens with asymmetric quantization if we do not apply clipping.

Instead, we can choose to _clip_ certain values. Clipping involves setting a different dynamic range of the original values such that all outliers get the same value.

In the example below, if we were to manually set the dynamic range to \[-5, 5\] all values outside that will either be mapped to -127 or to 127 regardless of their value:

[![Image 28](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52511453-ca48-42ca-9818-d1afa6dd7369_1120x408.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52511453-ca48-42ca-9818-d1afa6dd7369_1120x408.png)

The major advantage is that the quantization error of the _non-outliers_ is reduced significantly. However, the quantization error of _outliers_ increases.

In the example, I showed a naive method of choosing an arbitrary range of \[-5, 5\]. The process of selecting this range is known as _calibration_ which aims to find a range that includes as many values as possible while minimizing the quantization error.

Performing this calibration step is not equal for all types of parameters.

We can view the weights and biases of an LLM as _static_ values since they are known before running the model. For instance, the [~20GB file of Llama 3](https://huggingface.co/meta-llama/Meta-Llama-3-8B/tree/main) consists mostly of its weight and biases.

[![Image 29](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d79e60e-92ea-4c91-bbdb-297c819cd821_1456x440.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d79e60e-92ea-4c91-bbdb-297c819cd821_1456x440.png)

Since there are significantly fewer biases (millions) than weights (billions), the biases are often kept in higher precision (such as INT16), and the main effort of quantization is put towards the weights.

For weights, which are static and known, calibration techniques for choosing the range include:

*   Manually chosing a _percentile_ of the input range
    
*   Optimize the _mean squared error_ (MSE) between the original and quantized weights.
    
*   Minimizing _entropy_ (KL-divergence) between the original and quantized values
    

[![Image 30](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff24238b2-de53-40c8-8869-9a7d83678544_772x312.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff24238b2-de53-40c8-8869-9a7d83678544_772x312.png)

Choosing a percentile, for instance, would lead to similar clipping behavior as we have seen before.

The input that is continuously updated throughout the LLM is typically referred to as “_activations_”.

[![Image 31](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6baaee7f-40dd-4f6a-9a8d-bd79a7b2abc7_1456x520.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6baaee7f-40dd-4f6a-9a8d-bd79a7b2abc7_1456x520.png)

Note that these values are called activations since they often go through some activation function, like sigmoid or relu.

Unlike weights, activations vary with each input data fed into the model during inference, making it challenging to quantize them accurately.

Since these values are updated after each hidden layer, we only know what they will be during inference as the input data passes through the model.

[![Image 32](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fbb4248-fc4f-4317-b13a-898976010536_1230x672.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fbb4248-fc4f-4317-b13a-898976010536_1230x672.png)

Broadly, there are two methods for calibrating the quantization method of the weights and activations:

*   Post-Training Quantization (PTQ)
    
    *   Quantization _**after**_ training
        
*   Quantization Aware Training (QAT)
    
    *   Quantization _**during**_ training/fine-tuning
        

One of the most popular quantization techniques is post-training quantization (PTQ). It involves quantizing a model’s parameters (both weights and activations) **after** training the model.

Quantization of the _weights_ is performed using either symmetric or asymmetric quantization.

Quantization of the _activations_, however, requires inference of the model to get their potential distribution since we do not know their range.

There are two forms of quantization of the activations:

*   _Dynamic_ Quantization
    
*   _Static_ Quantization
    

After data passes a hidden layer, its activations are collected:

[![Image 33](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa3761f-0244-48f7-af56-5fb6c1cdd952_1476x756.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa3761f-0244-48f7-af56-5fb6c1cdd952_1476x756.png)

This distribution of activations is then used to calculate the _zeropoint_ (_**z**_) and _scale factor_ (**s**) values needed to quantize the output:

[![Image 34](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa593d70-c28a-43e3-b32c-5c7e46186408_1476x876.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa593d70-c28a-43e3-b32c-5c7e46186408_1476x876.png)

The process is repeated each time data passes through a new layer. Therefore, each layer has its own separate _**z**_ and _**s**_ values and therefore different quantization schemes.

In contrast to dynamic quantization, static quantization does not calculate the _zeropoint_ (_**z**_) and scale factor (_**s**_) during inference but beforehand.

To find those values, a **calibration dataset** is used and given to the model to collect these potential distributions.

[![Image 35](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dd6825-2a1c-459e-88c0-022a01dcebf2_1194x636.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dd6825-2a1c-459e-88c0-022a01dcebf2_1194x636.png)

After these values have been collected, we can calculate the necessary _**s**_ and _**z**_ values to perform quantization during inference.

When you are performing actual inference, the _**s**_ and _**z**_ values are not recalculated but are used globally over all activations to quantize them.

In general, dynamic quantization tends to be a bit more accurate since it only attempts to calculate the _**s**_ and _**z**_ values per hidden layer. However, it might increase compute time as these values need to be calculated.

In contrast, static quantization is less accurate but is faster as it already knows the _**s**_ and _**z**_ values used for quantization.

Going below 8-bit quantization has proved to be a difficult task as the quantization error increases with each loss of bit. Fortunately, there are several smart ways to reduce the bits to 6, 4, and even 2-bits (although going lower than 4-bits using these methods is typically not advised).

We will explore two methods that are commonly shared on HuggingFace:

*   _GPTQ_ (full model on GPU)
    
*   _GGUF_ (potentially offload layers on the CPU)
    

GPTQ is arguably one of the most well-known methods used in practice for quantization to 4-bits.[1](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#footnote-1-145531349)

It uses asymmetric quantization and does so layer by layer such that each layer is processed independently before continuing to the next:

[![Image 36](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc260ef95-2dbf-4f7e-80ba-213ce6623fcd_1230x816.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc260ef95-2dbf-4f7e-80ba-213ce6623fcd_1230x816.png)

During this layer-wise quantization process, it first converts the layer’s weights into the inverse-**Hessian**. It is a second-order derivative of the model’s loss function and tells us how sensitive the model's output is to changes in each weight.

Simplified, it essentially demonstrates the (_inverse_) **importance of each weight** in a layer.

Weights associated with smaller values in the Hessian matrix are more crucial because small changes in these weights can lead to significant changes in the model's performance.

[![Image 37](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad39a51b-e47f-44ec-af23-474292719be3_1440x696.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad39a51b-e47f-44ec-af23-474292719be3_1440x696.png)

In the inverse-Hessian, lower values indicate more “important” weights.

Next, we quantize and then dequantize the weight of the first row in our weight matrix:

[![Image 38](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eac2072-f4a5-42ca-a251-f934a57d2df5_1146x438.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eac2072-f4a5-42ca-a251-f934a57d2df5_1146x438.png)

This process allows us to calculate the **quantization error (**_**q**_**)** which we can weigh using the inverse-Hessian (_**h\_1**)_ that we calculated beforehand.

Essentially, we are creating a weighted-quantization error based on the importance of the weight:

[![Image 39](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd4b12b9-8b1b-4aa5-8d8c-ab8c1ab23671_1096x332.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd4b12b9-8b1b-4aa5-8d8c-ab8c1ab23671_1096x332.png)

Next, we redistribute this weighted quantization error over the other weights in the row. This allows for maintaining the overall function and output of the network.

For example, if we were to do this for the second weight, namely .3 (_**x\_2**_), we would add the quantization error (_**q**_) multiplied by the inverse-Hessian of the second weight (_**h**_**\_2**)

[![Image 40](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86456fdb-ba8f-4545-aa45-a0f4d4c59362_1096x244.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86456fdb-ba8f-4545-aa45-a0f4d4c59362_1096x244.png)

We can do the same process over the third weight in the given row:

[![Image 41](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf47538b-4a3b-48df-9dbd-dded0ed09ce4_1284x438.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf47538b-4a3b-48df-9dbd-dded0ed09ce4_1284x438.png)

We iterate over this process of redistributing the weighted quantization error until all values are quantized.

This works so well because weights are typically related to one another. So when one weight has a quantization error, related weights are updated accordingly (through the inverse-Hessian).

> **NOTE**: [The authors](https://arxiv.org/pdf/2210.17323) used several tricks to speed up computation and improve performance, such as adding a dampening factor to the Hessian, “lazy batching”, and precomputing information using the Cholesky method. I would highly advise checking out [this YouTube video](https://www.youtube.com/watch?v=mii-xFaPCrA) on the subject.

> **TIP**: Check out [EXL2](https://github.com/turboderp/exllamav2) if you want a quantization method aimed at performance optimizations and improving inference speed.

While GPTQ is a great quantization method to run your full LLM on a GPU, you might not always have that capacity. Instead, we can use GGUF to offload any layer of the LLM to the CPU. [2](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#footnote-2-145531349)

This allows you to use both the CPU and GPU when you do not have enough VRAM.

The quantization method GGUF is updated frequently and might depend on the level of bit quantization. However, the general principle is as follows.

First, the weights of a given layer are split into “super” blocks each containing a set of “sub” blocks. From these blocks, we extract the scale factor (_**s**_) and alpha (_**α**_):

[![Image 42](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98047d62-3925-4a29-a23b-c5bfa517f073_894x480.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98047d62-3925-4a29-a23b-c5bfa517f073_894x480.png)

To quantize a given “sub” block, we can use the _absmax_ quantization we used before. Remember that it multiplies a given weight by the scale factor **(**_**s**_**)**:

[![Image 43](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf159bb5-8158-43e3-bae1-8812fc0fa146_1096x120.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf159bb5-8158-43e3-bae1-8812fc0fa146_1096x120.png)

The scale factor is calculated using the information from the “sub” block but is quantized using the information from the “super” block which has its own scale factor:

[![Image 44](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3e7f68b-6ce8-45ba-a844-80b5eb0ab2d3_1096x196.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3e7f68b-6ce8-45ba-a844-80b5eb0ab2d3_1096x196.png)

This block-wise quantization uses the scale factor (**s\_super**) from the “super” block to quantize the scale factor (**s\_sub**) from the “sub” block.

The quantization level of each scale factor might differ with the “super” block generally having a higher precision than the scale factor of the “sub” block.

To illustrate, let’s explore a couple of quantization levels (2-bit, 4-bit, and 6-bit):

[![Image 45](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43ca3393-869a-4be3-bf8b-0c52e42017d7_1984x692.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43ca3393-869a-4be3-bf8b-0c52e42017d7_1984x692.png)

**NOTE**: Depending on the quantization type, an additional minimum value (_**m**_) is needed to adjust the zero-point. These are quantized the same as the scale factor (_**s**_).

Check out [the original pull request](https://github.com/ggerganov/llama.cpp/pull/1684) for an overview of all quantization levels. Also, see [this pull request](https://github.com/ggerganov/llama.cpp/pull/4861) for more information on quantization using importance matrices.

In Part 3, we saw how we could quantize a model _**after**_ training. A downside to this approach is that this quantization does not consider the actual training process.

This is where Quantization Aware Training (QAT) comes in. Instead of quantizing a model _**after**_ it was trained with post-training quantization (PTQ), QAT aims to learn the quantization procedure _**during**_ training.

[![Image 46](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad4fa3b-b440-4be3-90bd-b66e219f191e_1368x810.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad4fa3b-b440-4be3-90bd-b66e219f191e_1368x810.png)

QAT tends to be more accurate than PTQ since the quantization was already considered during training. It works as follows:

During training, so-called “_fake_” quants are introduced. This is the process of first quantizing the weights to, for example, INT4 and then dequantizing back to FP32:

[![Image 47](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3a17734-65f8-45d7-8e4e-f7bc1c592577_1824x360.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3a17734-65f8-45d7-8e4e-f7bc1c592577_1824x360.png)

This process allows the model to consider the quantization process during training, the calculation of loss, and weight updates.

QAT attempts to explore the loss landscape for “_wide_” minima to minimize the quantization errors as “_narrow_” minima tend to result in larger quantization errors.

[![Image 48](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa70ee37e-3b4f-4598-8eef-2a9ab13658c1_1200x640.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa70ee37e-3b4f-4598-8eef-2a9ab13658c1_1200x640.png)

For example, imagine if we did not consider quantization during the backward pass. We choose the weight with the smallest loss according to gradient descent. However, that would introduce a larger quantization error if it’s in a “_narrow_” minima.

In contrast, if we consider quantization, a different updated weight will be selected in a “_wide_” minima with a much lower quantization error.

[![Image 49](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb26d3f00-f599-4c75-beb4-21d87625b1d8_1200x640.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb26d3f00-f599-4c75-beb4-21d87625b1d8_1200x640.png)

As such, although PTQ has a lower loss in high precision (e.g., FP32), QAT results in a lower loss in lower precision (e.g., INT4) which is what we aim for.

Going to 4-bits as we saw before is already quite small but what if we were to reduce it even further?

This is where [BitNet](https://arxiv.org/pdf/2310.11453) comes in, representing the weights of a model single 1-bit, using either **\-1** or **1** for a given weight.[3](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#footnote-3-145531349)

It does so by injecting the quantization process directly into the Transformer architecture.

Remember that the Transformer architecture is used as the foundation of most LLMs and is composed of computations that involve linear layers:

[![Image 50](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3587e75-d631-4ecd-8da9-26fedfc68c53_1364x768.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3587e75-d631-4ecd-8da9-26fedfc68c53_1364x768.png)

These linear layers are generally represented with higher precision, like FP16, and are where most of the weights reside.

BitNet replaces these linear layers with something they call the **BitLlinear**:

[![Image 51](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6b8cbbf-057d-46c9-b275-dab262dd78d5_1364x768.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6b8cbbf-057d-46c9-b275-dab262dd78d5_1364x768.png)

A BitLinear layer works the same as a regular linear layer and calculates the output based on the weights multiplied by the activation.

In contrast, a BitLinear layer represents the weights of a model using 1-bit and activations using INT8:

[![Image 52](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9806feb5-2212-4fc3-af0b-ef42ae536787_1240x552.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9806feb5-2212-4fc3-af0b-ef42ae536787_1240x552.png)

A BitLinear layer, like Quantization-Aware Training (QAT) performs a form of “fake” quantization during training to analyze the effect of quantization of the weights and activations:

[![Image 53](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25935e2a-7643-4705-8961-0b40506fe757_1296x832.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25935e2a-7643-4705-8961-0b40506fe757_1296x832.png)

**NOTE**: In the paper they used **γ** instead of **α** but since we used a throughout our examples, I’m using that. Also, note that **β** is not the same as we used in zero-point quantization but the average absolute value.

Let’s go through the BitLinear step-by-step.

While training, the weights are stored in INT8 and then quantized to 1-bit using a basic strategy, called the _signum function._

In essence, it moves the distribution of weights to be centered around 0 and then assigns everything left to 0 to be -1 and everything to the right to be 1:

[![Image 54](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1080b79-6d3c-4dde-a6f1-a354afae4f54_1152x508.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1080b79-6d3c-4dde-a6f1-a354afae4f54_1152x508.png)

Additionally, it tracks a value **β (**_average_ absolute value**)** that we will use later on for dequantization.

To quantize the activations, BitLinear makes use of _absmax quantization_ to convert the activations from FP16 to INT8 as they need to be in higher precision for the matrix multiplication (×).

[![Image 55](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc69928b-3169-4c35-963b-c25ec218bc12_1260x552.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc69928b-3169-4c35-963b-c25ec218bc12_1260x552.png)

Additionally, it tracks **α (**_highest_ absolute value**)** that we will use later on for dequantization.

We tracked **α (**_highest absolute value of activations_**)** and **β (**_average absolute value of weights_**)** as those values will help us dequantize the activations back to FP16.

The output activations are rescaled with {**α**, γ} to dequantize them to the original precision:

[![Image 56](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F330cb1bb-9a98-45c1-b140-0fa8038d521f_1296x404.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F330cb1bb-9a98-45c1-b140-0fa8038d521f_1296x404.png)

And that’s it! This procedure is relatively straightforward and allows models to be represented with only two values, either **\-1** or **1**.

Using this procedure, the authors observed that as the model size grows, the smaller the performance gap between a 1-bit and FP16-trained becomes.

However, this is only for larger models (>30B parameters) and the gab with smaller models is still quite large.

[BitNet 1.58b](https://arxiv.org/pdf/2402.17764) was introduced to improve upon the scaling issue previously mentioned.[4](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#footnote-4-145531349)

In this new method, every single weight of the model is not just **\-1** or **1**, but can now also take **0** as a value, making it _ternary_. Interestingly, adding just the **0** greatly improves upon BitNet and allows for much faster computation.

So why is adding 0 such a major improvement?

It has everything to do with _matrix multiplication_!

First, let’s explore how matrix multiplication in general works. When calculating the output, we multiply a weight matrix by an input vector. Below, the first multiplication of the first layer of a weight matrix is visualized:

[![Image 57](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f3a7393-5ad4-4375-8382-197c7a5aa442_1048x360.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f3a7393-5ad4-4375-8382-197c7a5aa442_1048x360.png)

Note that this multiplication involves two actions, **multiplying** individual weights with the input and then **adding** them all together.

BitNet 1.58b, in contrast, manages to forego the act of multiplication since ternary weights essentially tell you the following:

*   1: I want to add this value
    
*   0: I do not want this value
    
*   \-1: I want to subtract this value
    

As a result, you only need to perform addition if your weights are quantized to 1.58 bit:

[![Image 58](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fed2720-9aa3-4b83-8ba7-4347b2fe1f0d_1048x360.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fed2720-9aa3-4b83-8ba7-4347b2fe1f0d_1048x360.png)

Not only can this speed up computation significantly, but it also allows for **feature filtering**.

By setting a given weight to 0 you can now ignore it instead of either adding or subtracting the weights as is the case with 1-bit representations.

To perform weight quantization BitNet 1.58b uses _absmean_ quantization which is a variation of the absmax quantization that we saw before.

It simply compresses the distribution of weights and uses the absolute mean (**α**) to quantize values. They are then rounded to either -1, 0, or 1:

[![Image 59](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facda9425-8b3d-47fe-92de-16c33e57613b_1108x512.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facda9425-8b3d-47fe-92de-16c33e57613b_1108x512.png)

Compared to BitNet the activation quantization is the same except for one thing. Instead of scaling the activations to range \[**0**, **2ᵇ⁻¹**\], they are now scaled to  
\[**\-2ᵇ⁻¹**, **2ᵇ⁻¹**\] instead using _absmax quantization_.

And that’s it! 1.58-bit quantization required (mostly) two tricks:

*   Adding **0** to create ternary representations \[-1, 0, 1\]
    
*   _absmean quantization_ for weights
    

“**13B** BitNet b1.58 is more efficient, in terms of latency, memory usage, and energy consumption than a **3B** FP16 LLM”

As a result, we get lightweight models due to having only 1.58 computationally efficient bits!

This concludes our journey in quantization! Hopefully, this post gives you a better understanding of the potential of quantization, GPTQ, GGUF, and BitNet. Who knows how small the models will be in the future?!

To see more visualizations related to LLMs and to support this newsletter, check out the book I’m writing with Jay Alammar. It will be released soon!

Hopefully, this was an accessible introduction to quantization! If you want to go deeper, I would suggest the following resources:

*   A HuggingFace blog about the **[LLM.int8()](https://huggingface.co/blog/hf-bitsandbytes-integration)** quantization method: you can find the paper [here](https://arxiv.org/pdf/2208.07339).
    
*   Another great HuggingFace blog about [quantization for](https://huggingface.co/blog/embedding-quantization) **[embeddings](https://huggingface.co/blog/embedding-quantization)**.
    
*   A blog about [Transformer Math 101](https://blog.eleuther.ai/transformer-math/), describing the basic math related to computation and memory usage for transformers.
    
*   [This](https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator) and [this](https://vram.asmirnov.xyz/) are two nice resources to calculate the (**V)RAM** you need for a given model.
    
*   If you want to know more about **QLoRA**[5](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization#footnote-5-145531349), a quantization technique for fine-tuning, it is covered extensively in my upcoming book: [Hands-On Large Language Models](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961).
    
*   A truly [amazing YouTube video](https://www.youtube.com/watch?v=mii-xFaPCrA) about **GPTQ** explained incredibly intuitively.
