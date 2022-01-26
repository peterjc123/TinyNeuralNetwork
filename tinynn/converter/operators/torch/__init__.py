
import typing
import torch

from .base import *
from .prim import *
from .aten import *
from .quantized import *

OPERATOR_CONVERTER_DICT: typing.Dict[str, OperatorConverter] = {"prim::Constant": PrimConstantConverter,
                                                                "prim::TupleConstruct": PrimTupleConstructConverter,
                                                                "prim::ListConstruct": PrimListConstructConverter,
                                                                "prim::ListUnpack": PrimListUnpackConverter,
                                                                "prim::GetAttr": PrimGetAttrConverter,
                                                                "prim::ConstantChunk": PrimConstantChunkConverter,
                                                                "prim::NumToTensor": PrimNumToTensorConverter,
                                                                "prim::If": PrimIfConverter,
                                                                "aten::__getitem__": PrimGetItemConverter,

                                                                # aten
                                                                "aten::t": ATenTOperator,
                                                                "aten::view": ATenViewOperator,
                                                                "aten::reshape": ATenReshapeOperator,
                                                                "aten::relu": ATenReluOperator,
                                                                "aten::relu_": ATenReluOperator,
                                                                "aten::relu6": ATenRelu6Operator,
                                                                "aten::relu6_": ATenRelu6Operator,
                                                                "aten::prelu": ATenPreluOperator,
                                                                "aten::leaky_relu": ATenLeakyReluOperator,
                                                                "aten::leaky_relu_": ATenLeakyReluOperator,
                                                                "aten::elu": ATenEluOperator,
                                                                "aten::elu_": ATenEluOperator,
                                                                "aten::conv2d": ATenConv2dOperator,
                                                                "aten::_convolution": ATenConvolutionOperator,
                                                                "aten::batch_norm": ATenBatchNormOperator,
                                                                "aten::avg_pool2d": ATenAvgPool2dOperator,
                                                                "aten::max_pool2d": ATenMaxPool2dOperator,
                                                                "aten::adaptive_avg_pool2d": ATenAdaptiveAvgPool2dOperator,
                                                                "aten::mean": ATenMeanOperator,
                                                                "aten::softmax": ATenSoftmaxOperator,
                                                                "aten::log_softmax": ATenLogSoftmaxOperator,
                                                                "aten::addmm": ATenAddmmOperator,
                                                                "aten::dropout": ATenDropoutOperator,
                                                                "aten::dropout_": ATenDropoutOperator,
                                                                "aten::contiguous": ATenContiguousOperator,
                                                                "aten::permute": ATenPermuteOperator,
                                                                "aten::sin": ATenSinOperator,
                                                                "aten::cos": ATenCosOperator,
                                                                "aten::tanh": ATenTanhOperator,
                                                                "aten::pow": ATenPowOperator,
                                                                "aten::sqrt": ATenSqrtOperator,
                                                                "aten::sigmoid": ATenSigmoidOperator,
                                                                "aten::add": ATenAddOperator,
                                                                "aten::add_": ATenAddOperator,
                                                                "aten::sub": ATenSubOperator,
                                                                "aten::sub_": ATenSubOperator,
                                                                "aten::mul": ATenMulOperator,
                                                                "aten::mul_": ATenMulOperator,
                                                                "aten::div": ATenDivOperator,
                                                                "aten::div_": ATenDivOperator,
                                                                "aten::reciprocal": ATenReciprocalOperator,
                                                                "aten::reciprocal_": ATenReciprocalOperator,
                                                                "aten::rsqrt": ATenRsqrtOperator,
                                                                "aten::rsqrt_": ATenRsqrtOperator,
                                                                "aten::atan2": ATenAtan2Operator,
                                                                "aten::constant_pad_nd": ATenConstantPadNdOperator,
                                                                "aten::reflection_pad1d": ATenReflectionPad1dOperator,
                                                                "aten::reflection_pad2d": ATenReflectionPad2dOperator,
                                                                "aten::select": ATenSelectOperator,
                                                                "aten::unsqueeze": ATenUnsqueezeOperator,
                                                                "aten::squeeze": ATenSqueezeOperator,
                                                                "aten::slice": ATenSliceOperator,
                                                                "aten::stack": ATenStackOperator,
                                                                "aten::cat": ATenCatOperator,
                                                                "aten::chunk": ATenChunkOperator,
                                                                "aten::embedding": ATenEmbeddingOperator,
                                                                "aten::linear": ATenLinearOperator,
                                                                "aten::lstm": ATenLstmOperator,
                                                                "aten::transpose": ATenTransposeOperator,
                                                                "aten::hardtanh": ATenHardtanhOperator,
                                                                "aten::hardtanh_": ATenHardtanhOperator,
                                                                "aten::flip": ATenFlipOperator,
                                                                "aten::floor": ATenFloorOperator,
                                                                "aten::floor_divide": ATenFloorDivideOperator,
                                                                "aten::leaky_relu": ATenLeakyReluOperator,
                                                                "aten::matmul": ATenMatmulOperator,
                                                                "aten::mm": ATenMmOperator,
                                                                "aten::flatten": ATenFlattenOperator,
                                                                "aten::upsample_bilinear2d": ATenUpsampleBilinear2dOperator,
                                                                "aten::upsample_nearest2d": ATenUpsampleNearest2dOperator,
                                                                "aten::clamp": ATenClampOperator,
                                                                "aten::exp": ATenExpOperator,
                                                                "aten::log": ATenLogOperator,
                                                                "aten::to": ATenToOperator,
                                                                "aten::ne": ATenNeOperator,
                                                                "aten::softplus": ATenSoftplusOperator,
                                                                "aten::layer_norm": ATenLayerNormOperator,
                                                                "aten::instance_norm": ATenInstanceNormOperator,
                                                                "aten::index": ATenIndexOperator,
                                                                "aten::clone": ATenCloneOperator,
                                                                "aten::repeat": ATenRepeatOperator,
                                                                "aten::hardswish": ATenHardswishOperator,
                                                                "aten::hardswish_": ATenHardswishOperator,
                                                                "aten::hardsigmoid": ATenHardsigmoidOperator,
                                                                "aten::hardsigmoid_": ATenHardsigmoidOperator,
                                                                "aten::silu": ATenSiluOperator,
                                                                "aten::silu_": ATenSiluOperator,
                                                                "aten::std": ATenStdOperator,
                                                                "aten::var": ATenVarOperator,
                                                                "aten::split": ATenSplitOperator,
                                                                "aten::split_with_sizes": ATenSplitWithSizesOperator,
                                                                "aten::pixel_shuffle": ATenPixelShuffleOperator,
                                                                "aten::pixel_unshuffle": ATenPixelUnshuffleOperator,
                                                                "aten::argmax": ATenArgmaxOperator,
                                                                "aten::argmin": ATenArgminOperator,
                                                                "aten::expand": ATenExpandOperator,
                                                                "aten::gather": ATenGatherOperator,
                                                                "aten::gelu": ATenGeluOperator,
                                                                "aten::gelu_": ATenGeluOperator,
                                                                "aten::copy_": ATenCopyOperator,
                                                                "aten::bmm": ATenBmmOperator,
                                                                "aten::eq": ATenEqOperator,
                                                                "aten::neg": ATenNegOperator,
                                                                "aten::bitwise_not": ATenBitwiseNotOperator,
                                                                "aten::bitwise_and": ATenBitwiseAndOperator,
                                                                "aten::bitwise_or": ATenBitwiseOrOperator,
                                                                "aten::__and__": ATenAndOperator,
                                                                "aten::__or__": ATenOrOperator,
                                                                "aten::sum": ATenSumOperator,
                                                                "aten::prod": ATenProdOperator,
                                                                "aten::min": ATenMinOperator,
                                                                "aten::max": ATenMaxOperator,
                                                                "aten::amin": ATenAminOperator,
                                                                "aten::amax": ATenAmaxOperator,
                                                                "aten::glu": ATenGluOperator,
                                                                "aten::glu_": ATenGluOperator,
                                                                "aten::masked_fill": ATenMaskedFillOperator,
                                                                "aten::masked_fill_": ATenMaskedFillOperator,
                                                                "aten::gt": ATenGtOperator,
                                                                "aten::lt": ATenLtOperator,
                                                                "aten::ge": ATenGeOperator,
                                                                "aten::le": ATenLeOperator,
                                                                "aten::remainder": ATenRemainderOperator,
                                                                "aten::where": ATenWhereOperator,

                                                                # quantized
                                                                "aten::quantize_per_tensor": ATenQuantizePerTensorOperator,
                                                                "aten::fake_quantize_per_tensor_affine": ATenFakeQuantizePerTensorAffineOperator,
                                                                "aten::fake_quantize_per_channel_affine": ATenFakeQuantizePerChannelAffineOperator,
                                                                "aten::quantized_lstm": ATenQuantizedLstmOperator,
                                                                "aten::dequantize": ATenDequantizeOperator,
                                                                "quantized::conv1d": QuantizedConv1dOperator,
                                                                "quantized::conv1d_relu": QuantizedConv1dReluOperator,
                                                                "quantized::conv2d": QuantizedConv2dOperator,
                                                                "quantized::conv2d_relu": QuantizedConv2dReluOperator,
                                                                "quantized::linear": QuantizedLinearOperator,
                                                                "quantized::linear_relu": QuantizedLinearReluOperator,
                                                                "quantized::relu6": QuantizedRelu6Operator,
                                                                "quantized::mul": QuantizedMulOperator,
                                                                "quantized::mul_scalar": QuantizedMulScalarOperator,
                                                                "quantized::cat": QuantizedCatOperator,
                                                                "quantized::batch_norm1d": QuantizedBatchNorm1dOperator,
                                                                "quantized::batch_norm2d": QuantizedBatchNorm2dOperator,
                                                                "quantized::batch_norm2d_relu": QuantizedBatchNorm2dReluOperator,
                                                                "quantized::add": QuantizedAddOperator,
                                                                "quantized::add_scalar": QuantizedAddScalarOperator,
                                                                "quantized::conv_transpose1d": QuantizedConvTranspose1dOperator,
                                                                "quantized::conv_transpose2d": QuantizedConvTranspose2dOperator,
                                                                "quantized::hardswish": QuantizedHardswishOperator,
                                                                "quantized::leaky_relu": QuantizedLeakyReluOperator,
                                                                "quantized::linear_dynamic": QuantizedLinearDynamicOperator,
                                                                "quantized::linear_relu_dynamic": QuantizedLinearReluDynamicOperator,

                                                                # non tracking
                                                                "aten::Int": NoTrackOperator,
                                                                "aten::zeros": NoTrackOperator,
                                                                "aten::detach": NoTrackOperator,
                                                                "aten::size": NoTrackOperator,
                                                                "aten::arange": NoTrackOperator,
                                                                "aten::ones": NoTrackOperator,
                                                                "aten::ones_like": NoTrackOperator,
                                                                "aten::zeros_like": NoTrackOperator,
                                                                "aten::empty": NoTrackOperator,
                                                                }
