classdef LinearLayer  
    properties  
        Weights  
        Bias  
        Input  
        Output  
        ActivationFunction  
    end  
    
    methods  
        function obj = LinearLayer(inputSize, outputSize)  
            % 初始化权重和偏置  
            obj.Weights = randn(outputSize, inputSize) * 0.01;  
            obj.Bias = zeros(outputSize, 1);  
            obj.ActivationFunction = @(x) max(0, x);  % ReLU  
        end  
        
        function [obj, output] = forward(obj, input)  
            obj.Input = input;  % 保存输入，用于反向传播  
            % 前向传播计算输出  
            output = obj.ActivationFunction(obj.Weights * input + obj.Bias);  
            obj.Output = output;  % 保存输出  
        end  
        
        function [obj, dInput, dWeights, dBias] = backward(obj, dOutput)  
            % 计算输入对损失的梯度  
            dInput = (obj.Weights' * dOutput) .* (obj.Input > 0);  % 对 ReLU 求导  
            dWeights = dOutput * obj.Input';  % 权重梯度  
            dBias = sum(dOutput, 2);  % 偏置梯度  
        end  
    end  
end