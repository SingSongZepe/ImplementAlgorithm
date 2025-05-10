classdef LinearLayer
    properties
        in_features    % input features
        out_features   % output features
        W              % parameters       s2 x s1
        b              % biases           s2 x 1
        input          % input numbers
    end
    
    methods
        function f = LinearLayer(in_features, out_features)
            f.in_features = in_features;
            f.out_features = out_features;
            f.W = ParameterInitialization.kaiming(in_features, out_features);
            f.b = BiasInitialization.random(out_features);
        end
            
        % e.g.
        % s1 = 3, s2 = 2
        %                W                     x
        % | w_{0, 0}, w_{1, 0}, w_{2, 0} |  | z_0 |
        % | w_{0, 1}, w_{1, 1}, w_{2, 1} |  | z_1 | 
        %                                   | z_2 | 
        function z = forward(f, x)  % x is column vector s1 x 1  
            f.input = x;              % Save input for backward pass  
            z = f.W * x + f.b;       % z is column vector s2 x 1  
        end  
        
        function [grad_input, f] = backward(f, lr, grad_out)  
            grad_W = grad_out * f.input';  % Gradient w.r.t. weights  
            grad_b = sum(grad_out, 2);      % Gradient w.r.t. biases  

            grad_input = f.W' * grad_out;    % Gradient w.r.t. input  

            f.W = f.W - lr * grad_W;         % Update weights  
            f.b = f.b - lr * grad_b;         % Update biases  
        end 
    end
end


