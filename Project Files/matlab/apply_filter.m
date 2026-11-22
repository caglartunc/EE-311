function y = apply_filter(b, a, x)
% APPLY_FILTER  Pass signal x through the filter [b, a].
y = filter(b, a, x);
end
