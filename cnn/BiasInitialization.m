classdef BiasInitialization

    methods (Static)
        % b  r x 1
        function b = zero(features)
            b = zeros(features, 1);
        end
        
        function b = random(features)
            b = rand(features, 1) * 2 - 1;
        end
    end

end