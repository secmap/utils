#==========================================================
#   read_test.py is the test for reading features
#   : you should specify the directory name of features while read()
#   : you should spechify which features are used in the dataset
#
#==========================================================
#from utils.FeatureReader import FeatureReader as fr
#traindata , trainlabel, testdata, testlabel  = fr(range(8), [0]*8, "features").read()
#print(traindata)
#
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer

class Dataset():
    def __init__(self, name):
        self.name = name
        self.traindata = None
        self.trainfile = None
        self.trainlabel = None
        self.testdata = None
        self.testfile = None
        self.testlabel = None

    def read(self, filename):
        try:
            with open(filename, 'rb') as f:
                a = np.load(f)
                self.traindata = a['train_data']
                self.trainfile = a['train_file']
                self.trainlabel = a['train_label']
                self.testdata = a['test_data']
                self.testfile = a['test_file']
                self.testlabel = a['test_label']
        except Exception as e:
            print(e)

class FeatureReader():
    def __init__(self, feature_choice, normalize_choice=None, dir_name='.'):
        self.features = ['api_bin.npz',
                        'bytes_1_gram.npz',
                        'bytes_2_gram.npz',
                        'entropy_bin.npz',
                        'header_bin.npz',
                        'iat_bin.npz',
                        'img1_bytes.npz',
                        'img2_bytes.npz',
                        'opcode_bin.npz',
                        'register_bin.npz',
                        'section_bin.npz',
                        'str_bin.npz']
        self.normalize = [lambda x : StandardScaler().fit_transform(x.astype(np.float64)),
                         lambda x : MinMaxScaler().fit_transform(x.astype(np.float64)),
                         lambda x : MaxAbsScaler().fit_transform(x.astype(np.float64)),
                         lambda x : RobustScaler(quantile_range=(25, 75)).fit_transform(x.astype(np.float64)),
                         lambda x : QuantileTransformer(output_distribution='uniform').fit_transform(x.astype(np.float64)),
                         lambda x : QuantileTransformer(output_distribution='normal').fit_transform(x.astype(np.float64)),
                         lambda x : Normalizer().fit_transform(x.astype(np.float64))]
        self.normalize_description = ['Data after standard scaling',
                                     'Data after min-max scaling',
                                     'Data after max-abs scaling',
                                     'Data after robust scaling',
                                     'Data after quantile transformation (uniform pdf)',
                                     'Data after quantile transformation (gaussian pdf)',
                                     'Data after sample-wise L2 normalizing']
        for i in range(len(feature_choice)):
            if feature_choice[i] >= len(self.features):
                print('index should be less than', len(self.features))
                return None
        if normalize_choice != None:
            for i in range(len(normalize_choice)):
                if normalize_choice[i] >= len(self.normalize):
                    print('index should be less than', len(self.features))
                    return None
        else:
            normalize_choice = [0] * len(feature_choice)
        self.feature_choice = feature_choice
        self.normalize_choice = normalize_choice
        self.dir_name = dir_name
        self.datasets = []
        self.con_traindata = None
        self.con_trainlabel = None
        self.con_testdata = None
        self.con_testlabel = None
        self._read()

    def index(self):
        print('Features index:')
        for i in range(len(self.features)):
            print(i, ':', self.features[i])
        print('Normalization index:')
        print(-1, ':', 'No normalization')
        for i in range(len(self.normalize_description)):
            print(i, ':', self.normalize_description[i])

    def concatenate(self):
        if self.datasets != []:
            self.con_traindata = self.datasets[0].traindata
            self.con_trainlabel = self.datasets[0].trainlabel
            self.con_testdata = self.datasets[0].testdata
            self.con_testlabel = self.datasets[0].testlabel

            for i in self.datasets[1:]:
                self.con_traindata = np.concatenate(
                    (self.con_traindata, i.traindata), axis=1)
                self.con_testdata = np.concatenate(
                    (self.con_testdata, i.testdata),axis=1)
    def _normalize(self):
        for i in range(len(self.datasets)):
            print(self.features[self.feature_choice[i]].split('.')[0], 'is doing', self.normalize_description[self.normalize_choice[i]][11:])
            self.datasets[i].traindata = self.normalize[self.normalize_choice[i]](self.datasets[i].traindata)
            self.datasets[i].testdata = self.normalize[self.normalize_choice[i]](self.datasets[i].testdata)

    def _read(self):
        for c in self.feature_choice:
            tf_name = self.dir_name+'/'+self.features[c]
            print("handling {}".format(tf_name))
            d = Dataset(tf_name.split('.')[0])
            d.read(tf_name)
            self.datasets.append(d)
        self._normalize()
        self.concatenate()

    def read(self):
        return self.con_traindata, self.con_trainlabel, self.con_testdata, self.con_testlabel
