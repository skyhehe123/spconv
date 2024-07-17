# spconv (group-wise subconv supported)

#### Linux

0. uninstall spconv and cumm installed by pip
1. install build-essential, install CUDA
2. ```git clone https://github.com/FindDefinition/cumm```, ```cd ./cumm```, ```pip install -e .```
3. ```git clone https://github.com/traveller59/spconv```, ```cd ./spconv```, ```pip install -e .```
4. in python, ```import spconv``` and wait for build finish.



### Build wheel from source (not recommend, this is done in CI.)

You need to rebuild ```cumm``` first if you are build along a CUDA version that not provided in prebuilts.

#### Linux

1. install build-essential, install CUDA
2. run ```export SPCONV_DISABLE_JIT="1"```
3. run ```pip install pccm cumm wheel```
4. run ```python setup.py bdist_wheel```+```pip install dists/xxx.whl```


## LICENSE

Apache 2.0
