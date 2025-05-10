
% use for digital recognizer
classdef Net
    properties
        fl1 % input to hidden 1
        fl2 % hidden 1 to hidden 2
        fl3 % hidden 2 to output
        lr  % learn rate
    end
    methods (Access = public)
        function net = Net(lr)
            net.fl1 = LinearLayer(1024, 128);
            net.fl2 = LinearLayer(128, 128);
            net.fl3 = LinearLayer(128, 10);
            net.lr  = lr;
        end
        
        % train process
        function x = forward(net, x)
            x = ReLU(net.fl1.forward(x));
            x = ReLU(net.fl2.forward(x));
            x = softmax(net.fl3.forward(x));
        end
        
        % pass result of forward to this function
        % it will use loss function to back propagation
        function net = backward(net, pred, targ)  
            dL_dpred = (pred - targ);   
   
            [dL_dhidden2, net.fl3] = net.fl3.backward(net.lr, dL_dpred);  
            [dL_dhidden1, net.fl2] = net.fl2.backward(net.lr, dL_dhidden2);   
            [~, net.fl1] = net.fl1.backward(net.lr, dL_dhidden1);   
        end

        % prediction
        function [pred_probability, pred_digit] = predict(net, x)
            [pred_probability, pred_digit] = max(net.forward(x));
        end
    end

end

