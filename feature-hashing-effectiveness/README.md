# The unreasonable effectiveness of feature hashing
Speaker: [Gianluca Campanella](https://github.com/gcampanella)

## Description

Feature hashing is a computationally efficient pre-processing technique for sparse, high-dimensional features. Starting from an overview of the method, this talk covers: the impact of hash functions, hash size and collisions on statistical performance; three libraries for model training with feature hashing; hash reversibility and its implications for model interpretability.

## Abstract

Most machine learning (ML) algorithms are trained on numerical vectors; however, training data frequently consist of categorical features or raw text that must be transformed before they can be used. For example, one-hot encoding is often applied to categorical features, whilst a bag-of-words representation is commonly used for text.

Feature hashing is an approximate technique for mapping sparse, high-dimensional features onto a fixed-size vector space. Rather than building a dictionary from the training data, it applies a hash function to compute feature indices directly. This makes it not only space-efficient but also well-suited to online learning scenarios. Collisions naturally occur in the typical use case where the hash space is much smaller than the original feature space, but don't appear to compromise the statistical performance of models trained on hashed features.

Despite its general applicability to many ML algorithms, feature hashing has found preferential adoption in conjunction with linear models such as linear and logistic regression. These models can be trained very efficiently on massive data sets, even in the presence of extremely sparse features. Interaction terms are straightforward to introduce in hash space and increase model expressiveness, achieving similar statistical performance to tree-based methods.

The ideas explored in this workshop are transferable skills to other applications in deep learning and provide a great stepping stone for those that have a good familiarity with deep learning in applications such as image classification and want to explore more advanced topics in deep learning.