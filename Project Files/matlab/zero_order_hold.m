function y = zero_order_hold(s, D)
% ZERO_ORDER_HOLD  Each sample held for D points on the original fine grid.
y = repelem(s(:), D);
end
