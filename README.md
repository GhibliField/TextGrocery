TextGrocery
===========

[![Build Status](https://travis-ci.org/2shou/TextGrocery.svg?branch=master)](https://travis-ci.org/2shou/TextGrocery)

A simple, efficient short-text classification tool based on LibLinear

Embed with [pynlpir](https://github.com/tsroten/pynlpir) as default tokenizer to support Chinese tokenize

Other languages: [更详细的中文文档](http://textgrocery.readthedocs.org/zh/latest/index.html)

**Using pynlpir to do Chinese segmentation to leverage the classification performance **

Performance
-----------
Better than native TextGrocery(using jieba)

Sample Code
-----------

```python
>>> from tgrocery import Grocery
# Create a grocery(don't forget to set a name)
>>> grocery = Grocery('sample')
# Train from list
>>> train_src = [
    ('education', 'Student debt to cost Britain billions within decades'),
    ('education', 'Chinese education for TV experiment'),
    ('sports', 'Middle East and Asia boost investment in top level sports'),
    ('sports', 'Summit Series look launches HBO Canada sports doc series: Mudhar')
]
>>> grocery.train(train_src)
# Or train from file
# Format: Label\tText
>>> grocery.train('train_ch.txt')
# Save model
>>> grocery.save()
# Load model(the same name as previous)
>>> new_grocery = Grocery('sample')
>>> new_grocery.load()
# Predict
>>> new_grocery.predict('Abbott government spends $8 million on higher education media blitz')
education
# Test from list
>>> test_src = [
    ('education', 'Abbott government spends $8 million on higher education media blitz'),
    ('sports', 'Middle East and Asia boost investment in top level sports'),
]
>>> new_grocery.test(test_src)
# Return Accuracy
1.0
# Or test from file
>>> new_grocery.test('test_ch.txt')
# Custom tokenize
>>> custom_grocery = Grocery('custom', custom_tokenize=list)
```

More examples: [sample/](sample/)

Install
-------

    $ pip install tgrocery

> Only test under Unix-based System


Specification
-------
if *Your license appears to have expired* ,you may [here](https://github.com/NLPIR-team/NLPIR/tree/master/License/license%20for%20a%20month/NLPIR-ICTCLAS%E5%88%86%E8%AF%8D%E7%B3%BB%E7%BB%9F%E6%8E%88%E6%9D%83) to download the license and put it into /pynlpir/data/
