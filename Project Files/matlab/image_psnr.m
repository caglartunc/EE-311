function p = image_psnr(ref, est)
% IMAGE_PSNR  PSNR in dB between two images with values in [0, 1].
mse = mean((ref(:) - est(:)).^2);
p = 10 * log10(1 / max(mse, 1e-12));
end
