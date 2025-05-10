classdef Net  
    properties  
        Layer1  
        Layer2  
        Layer3  
    end  
    
    methods  
        function obj = Net()  
            obj.Layer1 = LinearLayer(1024, 128); % 第一层  
            obj.Layer2 = LinearLayer(128, 128);  % 第二层  
            obj.Layer3 = LinearLayer(128, 10);    % 第三层 (输出层)  
        end  
        
        function output = forward(obj, input)  
            output = obj.Layer1.forward(input);  
            output = obj.Layer2.forward(output);  
            output = obj.Layer3.forward(output);  
            output = exp(output) ./ sum(exp(output), 1);  % Softmax  
        end  
        
        function [loss, dLoss] = computeLoss(output, labels)  
            % 计算交叉熵损失  
            m = size(output, 2);  % 批处理大小  
            loss = -sum(log(output(labels + 1) + 1e-10)) / m;  % labels是从0开始的  
            dLoss = output;  % Softmax的导数（Jacobians）  
            dLoss(labels + 1) = dLoss(labels + 1) - 1;  % 交叉熵的链式法则  
            dLoss = dLoss / m;  % 平均  
        end  
        
        function updateWeights(obj, learningRate)  
            % 使用计算出的梯度更新权重  
            [obj.Layer3, dOutput3, dBias3] = obj.Layer3.backward(obj.Layer3.Output);  
            [obj.Layer2, dOutput2, dBias2] = obj.Layer2.backward(dOutput3);  
            [obj.Layer1, dOutput1, dBias1] = obj.Layer1.backward(dOutput2);  
            
            % 更新权重和偏置  
            obj.Layer3.Weights = obj.Layer3.Weights - learningRate * dOutput3;  
            obj.Layer3.Bias = obj.Layer3.Bias - learningRate * dBias3;  
            obj.Layer2.Weights = obj.Layer2.Weights - learningRate * dOutput2;  
            obj.Layer2.Bias = obj.Layer2.Bias - learningRate * dBias2;  
            obj.Layer1.Weights = obj.Layer1.Weights - learningRate * dOutput1;  
            obj.Layer1.Bias = obj.Layer1.Bias - learningRate * dBias1;  
        end  
    end  
end 