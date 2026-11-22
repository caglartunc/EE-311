function v = pulses_to_values(y, sps)
% PULSES_TO_VALUES  One value per pulse: the average of the second half of each pulse.
K = floor(numel(y) / sps);
Y = reshape(y(1:K*sps), sps, K);
v = mean(Y(floor(sps/2)+1:end, :), 1).';
end
