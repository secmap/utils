#==========================================================
#   read_test.py is the test for reading features
#   : you should specify the directory name of features while read()
#   : you should spechify which features are used in the dataset
#
#==========================================================
#from utils.FeatureReader import FeatureReader as fr
#traindata , trainlabel, testdata, testlabel  = fr(range(8)).read("features")
#print(traindata)
#
import numpy as np

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
                self.testlabel = a['test_file']
        except Exception as e:
            print(e)

class FeatureReader():
    def __init__(self, choose):
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
        for i in range(len(choose)):
            if choose[i] >= len(self.features):
                print('index should be less than', len(self.features))
                return None
        self.choose = choose
        self.datasets = []
        self.con_traindata = None
        self.con_trainlabel = None
        self.con_testdata = None
        self.con_testlabel = None

    def index(self):
        for i in range(len(self.features)):
            print(i, ':', self.features[i])

    def concatenate(self):
        if self.datasets != []:
            self.con_traindata = self.datasets[0].traindata
            self.con_trainlabel = self.datasets[0].trainlabel
            self.con_testdata = self.datasets[0].testdata
            self.con_testlabel = self.datasets[0].testlabel

            for i in self.datasets[1:]:
                self.con_traindata = np.concatenate(
                    (self.con_traindata, i.traindata), axis=1)
                self.con_trainlabel = np.concatenate(
                    (self.con_trainlabel, i.trainlabel), axis=1)
                self.con_testdata = np.concatenate(
                    (self.con_testdata, i.testdata),axis=1)
                self.con_testlabel = np.concatenate(
                    (self.con_testlabel, i.testlabel), axis=1)

    def read(self, dir_name):
        for c in self.choose:
            tf_name = dir_name+'/'+self.features[c]
            print("handling {}".format(tf_name))
            d = Dataset(tf_name.split('.')[0])
            d.read(tf_name)
            self.datasets.append(d)
        self.concatenate()
        return self.con_traindata, self.con_trainlabel, self.con_testdata, self.con_testlabel
