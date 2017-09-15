# FeatureReader

## Usage
```
>>> FeatureReader([]).index()
Features index:
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
Normalization index:
-1 : No normalization
0 : Data after standard scaling
1 : Data after min-max scaling
2 : Data after max-abs scaling
3 : Data after robust scaling
4 : Data after quantile transformation (uniform pdf)
5 : Data after quantile transformation (gaussian pdf)
6 : Data after sample-wise L2 normalizing

>>> f = FeatureReader(range(12))
handling ./api_bin.npz
handling ./bytes_1_gram.npz
handling ./bytes_2_gram.npz
handling ./entropy_bin.npz
handling ./header_bin.npz
handling ./iat_bin.npz
handling ./img1_bytes.npz
handling ./img2_bytes.npz
handling ./opcode_bin.npz
handling ./register_bin.npz
handling ./section_bin.npz
handling ./str_bin.npz
api_bin is doing standard scaling
bytes_1_gram is doing standard scaling
bytes_2_gram is doing standard scaling
entropy_bin is doing standard scaling
header_bin is doing standard scaling
iat_bin is doing standard scaling
img1_bytes is doing standard scaling
img2_bytes is doing standard scaling
opcode_bin is doing standard scaling
register_bin is doing standard scaling
section_bin is doing standard scaling
str_bin is doing standard scaling

>>> traindata , trainlabel, testdata, testlabel = f.read()
>>> traindata
array([[-0.3397555 , -0.24372368, -0.43646816, ..., -0.14354486,
        -0.18495664, -0.13413921],
       [ 0.87239435,  2.17603706,  1.70570685, ..., -0.14354486,
        -0.18495664,  0.1441579 ],
       [-0.3397555 , -0.24372368, -0.43646816, ..., -0.14354486,
        -0.18495664, -0.13413921],
       ...,
       [-0.3397555 , -0.24372368, -0.43646816, ...,  0.67906177,
         0.52916167, -0.13413921],
       [-0.3397555 , -0.24372368, -0.43646816, ...,  8.08252145,
         6.95622652,  0.70075211],
       [-0.3397555 , -0.24372368, -0.43646816, ..., -0.14354486,
        -0.18495664, -0.13413921]])
>>> trainlabel
array([0, 0, 0, ..., 1, 1, 1])
>>> testdata
array([[-0.00794127, -0.2900157 , -0.43274406, ..., -0.16959712,
        -0.09858896,  0.18109593],
       [-0.22701069, -0.2900157 , -0.43274406, ..., -0.16959712,
        -0.09858896, -0.13773494],
       [-0.3365454 , -0.2900157 , -0.43274406, ..., -0.16959712,
        -0.09858896, -0.13773494],
       ...,
       [-0.3365454 , -0.2900157 , -0.04306008, ..., -0.16959712,
        -0.09858896, -0.13773494],
       [-0.3365454 , -0.2900157 , -0.43274406, ...,  1.52637408,
         0.20758794,  0.18109593],
       [-0.3365454 , -0.2900157 , -0.43274406, ..., -0.16959712,
        -0.09858896, -0.13773494]])
>>> testlabel
array([0, 0, 0, ..., 1, 1, 1])
```
