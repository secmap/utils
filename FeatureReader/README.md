# FeatureReader

## Usage
```
FeatureReader([]).index()
0 : api_bin.npz
1 : bytes_1_gram.npz
2 : bytes_2_gram.npz
3 : entropy_bin.npz
4 : header_bin.npz
5 : iat_bin.npz
6 : img1_bytes.npz
7 : img2_bytes.npz
8 : opcode_bin.npz
9 : register_bin.npz
10 : section_bin.npz
11 : str_bin.npz

traindata , trainlabel, testdata, testlabel = FeatureReader([0,3,6,9]).read()
```
