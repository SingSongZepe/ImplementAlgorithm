function loss = crossEntropyLoss(pred, targ)  
    loss = -sum(targ .* log(pred + 1e-10));
end