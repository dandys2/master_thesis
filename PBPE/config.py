dataset = 'UBC'
batch_size = 32
k = 50
centers = None
thresh = 10  # in cm
numPoints = 2048  # number of points in each pcl
# TODO zajtra SV 11subs
singleview = False
# test_method = '11subjects'
test_method = 'random25'
leaveout = 12

# do NOT set both to True at once
segnet = False
mymodel = True

stepss = None

assert not segnet or not mymodel

if dataset == 'MHAD':
    poolTo1 = True
    globalAvg = False
    if singleview:
        numTrainSamples = 210917
        numTestSamples = 70305
    # elif test_method == '11subjects':
    #     numTrainSamples = 128865
    #     numTestSamples = 11746
    else:
        numTrainSamples = 105459
        numTestSamples = 35152
    numValSamples = 0

    numJoints = 29  # 35
    numRegions = numJoints
    fill = 6
elif dataset == 'UBC':
    poolTo1 = False  # False
    globalAvg = True
    if singleview:
        numTrainSamples = 177177
        numValSamples = 57057
        numTestSamples = 57057
    else:
        numTrainSamples = 59059
        numValSamples = 19019
        numTestSamples = 19019

    numJoints = 18
    numRegions = 18
    fill = 5
elif dataset == 'ITOP':
    poolTo1 = False
    globalAvg = True
    numTrainSamples = 17991
    numValSamples = 0
    numTestSamples = 4863

    numJoints = 15
    numRegions = 15
    fill = 6
else:  # 'CMU'
    poolTo1 = False
    globalAvg = True
    numTrainSamples = 112596
    numValSamples = 0
    numTestSamples = 28148

    numJoints = 15
    numRegions = 15
    fill = 6

# pcls_min = [1000000, 1000000, 1000000]
# pcls_max = [-1000000, -1000000, -1000000]
#
# poses_min = [1000000, 1000000, 1000000]
# poses_max = [-1000000, -1000000, -1000000]

# if singleview and segnet:
#     stepss = 4000

st = '_4000steps' if stepss is not None else ''
view = 'SV_' if singleview else ''
jts = '35j' if numJoints == 35 else ''
if segnet:
    name = view + ('11subs' + str(leaveout) + '_' if (
            dataset == 'MHAD' and test_method == '11subjects') else '') + jts + 'segnet_lr0.001_4residuals_2.blockconvs512' + st
elif mymodel:
    name = view + ('11subs' + str(leaveout) + '_' if (
            dataset == 'MHAD' and test_method == '11subjects') else '') + jts + 'mymodel_lr0.001_noproto_convs1x1_512_256_1residual_' + (
               'poolto1' if poolTo1 else 'nomaxpool') + (
               '_globalavgpool' if globalAvg else '') + '_4chan_reg_preds'
else:
    name = view + ('11subs' + str(leaveout) + '_' if (
            dataset == 'MHAD' and test_method == '11subjects') else '') + jts + 'pbpe_new_mae_denserelu_bnsegonly_weights1.01_lrdrop0.8_lr0.0005_3localfeats_woseq6_localzeromean'
    # name = 'pbpe_orig'

# use predicted regions when running 4-chan model - only applied when using generator
if mymodel and (dataset in ['MHAD', 'UBC']):
    predicted_regs = True
else:
    predicted_regs = False

workers = 4  # mp.cpu_count()
