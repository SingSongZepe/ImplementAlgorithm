classdef ParameterInitialization
    
    methods (Static)
        % mode         'fan_in', 'fan_out'
        % nonlinearity 'relu'
        % W is a matrix   out x in
        function W = kaiming(in_features, out_features, varargin)
            p = inputParser;  
            
            addParameter(p, "mode", 'fan_in');  
            addParameter(p, "nonlinearity", 'relu');  
            
            parse(p, varargin{:});  
            
            mode = p.Results.mode;  
            nonlinearity = p.Results.nonlinearity;  

            if ~strcmp(nonlinearity, 'relu')
                error('onlt "relu" nonlinearity is accepted');
            end

            if strcmp(mode, 'fan_out')
                variance = 2 / out_features;
            else  % default mode
                variance = 2 / in_features;
            end
            
            W = normrnd(0, sqrt(variance), in_features, out_features)';
        end
        
        % xavier initialize
        function W = xavier(in_features, out_features)
            limit = sqrt(6 / (in_features + out_features));
            W = unifrnd(-limit, limit, in_features, out_features)';
        end
        
        % uniform distribution
        function W = randomUniform(in_features, out_features)
            W = (rand(in_features, out_features) * 2 - 1)';
        end
    
        % Guassian distribution, not recommended
        function W = randomNormal(in_features, out_features)
            W = randn(in_features, out_features)';
        end
    end

end