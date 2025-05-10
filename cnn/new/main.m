
clc; clear; cd("F://MySelf/Code/algorithm/cnn/new/");

train_set = load("./Data/trainFeatures.mat").trainFeatures;  
train_set_label = load("./Data/trainLabels.mat").trainLabels;  
test_set = load('./Data/valFeatures.mat').valFeatures;  
test_set_label = load('./Data/valLabels.mat').valLabels;  

train_set_label = train_set_label - 1;   
test_set_label = test_set_label - 1;  

net = Net();  
learningRate = 0.01;  
numEpochs = 1000;  
batchSize = 32;  

for epoch = 1:numEpochs  
    for i = 1:batchSize:size(train_set, 1)  
        batchInputs = train_set(i:min(i + batchSize - 1, end), :)';  
        batchLabels = train_set_label(i:min(i + batchSize - 1, end));  
        
        output = net.forward(batchInputs);  
         
        [loss, dLoss] = net.computeLoss(output, batchLabels);  
        net.updateWeights(learningRate);  
    end  
    
    if mod(epoch, 100) == 0  
        fprintf('Epoch %d, Loss: %.4f\n', epoch, loss);  
    end  
end  

predictions = net.forward(test_set');  
[~, predictedLabels] = max(predictions, [], 1);  
accuracy = sum(predictedLabels' - test_set_label == 0) / length(test_set_label);  
fprintf('Test accuracy: %.2f%%\n', accuracy * 100);  

