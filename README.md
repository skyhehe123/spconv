# spconv (group-wise subconv supported)

#### Linux

1. install build-essential, install CUDA
2. run ```export SPCONV_DISABLE_JIT="1"```
3. run ```pip install pccm cumm wheel```
4. run ```python setup.py bdist_wheel```+```pip install dists/xxx.whl```

#### QA
If you compile spconv successfully, but found the following error when import spconv.pytorch:

```ImportError: arg(): could not convert default argument 'workspace: tv::Tensor' in method '<class 'spconv.core_cc.csrc.sparse.convops.gemmops.GemmTunerSimple'>.run_with_tuned_result' into a Python object (type not registered yet?)```

it is because the cumm does not match the cuda version. Please rebuild the ```cumm``` by running

```git clone https://github.com/FindDefinition/cumm```, ```cd ./cumm```, ```pip install -e .```

## LICENSE

Apache 2.0
