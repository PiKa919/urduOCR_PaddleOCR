import paddle
gpu_available  = paddle.device.is_compiled_with_cuda()
print("GPU available:", gpu_available)