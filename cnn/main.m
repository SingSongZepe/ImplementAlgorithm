
% simple BP propagration
% implemented by SingSongZepe
% digit recognizer
% main file
clc; clear; cd("F://MySelf/Code/algorithm/cnn/");

% train data
train_set = load("./Data/trainFeatures.mat").trainFeatures;
train_set_label = load("./Data/trainLabels.mat").trainLabels;

% size
[train_cnt, train_pic_size]= size(train_set);

% learn rate
lr = 0.01;

net = Net(lr);

% epoch
for epoch = 1:2
    
    % start to train net
    for idx = 1: train_cnt
        train_pic = train_set(idx, :);
        train_label = train_set_label(idx);
        targ = zeros(10, 1);
        targ(train_label + 1) = 1;
        
        % need column vector
        pred = net.forward(train_pic');
        net = net.backward(pred, targ);

    end
end

% test data
test_set = load('./Data/valFeatures.mat').valFeatures;
test_set_label = load('./Data/valLabels.mat').valLabels;









