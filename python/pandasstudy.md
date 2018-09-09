# Pandas

## data structures

### Series

Series is a one - dimensional labeled array capable of holding any data type.

`s = pd.Series(data, index = index)`

data can be many different things:

* a Python dict
* an ndarray
* a scalar value

Series can also habe a _name_ attribute.

### DataFrame

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

DataFrame accepts many different kinds of input:

* Dict of 1D ndarray, lists, dicts, or Series
* 2-D numpy.ndarray
* Structured or record ndarray
* A Series
* Another DataFrame
