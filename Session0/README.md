## 1. What are Channels and Kernels (according to EVA)?

**Ans**: 
- A channel is a set of similiar features. For instance, consider repository of hand written alphabets; all these alphabets have common features. These features could be specific
 kind of edges that make up these alphabets. These features could be specific shapes that make up these alphabets. For example, P is made up of a round shape on top and a 
 vertical line in left half; B is made of a round shape on top, a round shape in bottom and a vertical line in left half. In this scenario, we can think of 3 channels, channel 
 1 will detect round shapes on top of P and B; channel 2 will detect round shape on bottom of B and channel 3 will detect vertical line in left half of both B and P. Similiarly,
 there can be a channel with all 45 degree tilted edges and another one with 60 degree tilted edges.
 
- Kernal is a feature extractor or a filter. Considering above example, Kernal is just a 3by3 matrix that convolves on top of image to give its features distributed 
across channels as output. The kernal convolves on top of alphabet P to extract 2 features that are sent to 2 channels - first feature is a round shape on top of P and second, 
vertical line in left half of P. 

## 2. Why should we (nearly) always use 3x3 kernels?
**Ans**: 3x3 kernels is good in extracting the edges in an image. First let's understand what is an edge, an edge is a move from black to white color in an image, from 
black to gray in an image, from dark gray to light gray in an image etc. The last 2 examples in this statement are also called as gradients. An Edge means that there is a pixel 
on an image that is surrounded by pixels of different shade on both sides; a black pixel surrounded by white on both sides is an edge. This kind of detection is not possible
with an even sized kernal - 2x2 or 4x4. We need to have a different shade in center and sides that can only happen with a odd numbered kernal size.
Secondly, a small kernal size means that number of parameters in the DNN layer are less; that in turn means less computation cost. 11x11 image can be reduced to 1x1 by using 
a 11x11 kernal that will involve 121 parameters (11 * 11). The same output (1x1 image) can be achived by using 5 3x3 kernals that means 45 params (5 * 3 * 3) which is way less
 than 121 parameters. Less params is equivalent to less computational cost.

## 3. How many times do we need to perform 3x3 convolutions operations to reach close to 1x1 from 199x199 (type each layer output like 199x199 > 197x197...)
**Ans**: We need to perform 99 3x3 convolutions. The idea is with every convolution, the image size gets reduced by 2x2.
199x199>197x197
197x197>195x195
195x195>193x193
193x193>191x191
191x191>189x189
189x189>187x187
187x187>185x185
185x185>183x183
183x183>181x181
181x181>179x179
179x179>177x177
177x177>175x175
175x175>173x173
173x173>171x171
171x171>169x169
169x169>167x167
167x167>165x165
165x165>163x163
163x163>161x161
161x161>159x159
159x159>157x157
157x157>155x155
155x155>153x153
153x153>151x151
151x151>149x149
149x149>147x147
147x147>145x145
145x145>143x143
143x143>141x141
141x141>139x139
139x139>137x137
137x137>135x135
135x135>133x133
133x133>131x131
131x131>129x129
129x129>127x127
127x127>125x125
125x125>123x123
123x123>121x121
121x121>119x119
119x119>117x117
117x117>115x115
115x115>113x113
113x113>111x111
111x111>109x109
109x109>107x107
107x107>105x105
105x105>103x103
103x103>101x101
101x101>99x99
99x99>97x97
97x97>95x95
95x95>93x93
93x93>91x91
91x91>89x89
89x89>87x87
87x87>85x85
85x85>83x83
83x83>81x81
81x81>79x79
79x79>77x77
77x77>75x75
75x75>73x73
73x73>71x71
71x71>69x69
69x69>67x67
67x67>65x65
65x65>63x63
63x63>61x61
61x61>59x59
59x59>57x57
57x57>55x55
55x55>53x53
53x53>51x51
51x51>49x49
49x49>47x47
47x47>45x45
45x45>43x43
43x43>41x41
41x41>39x39
39x39>37x37
37x37>35x35
35x35>33x33
33x33>31x31
31x31>29x29
29x29>27x27
27x27>25x25
25x25>23x23
23x23>21x21
21x21>19x19
19x19>17x17
17x17>15x15
15x15>13x13
13x13>11x11
11x11>9x9
9x9>7x7
7x7>5x5
5x5>3x3
3x3>1x1

```
x=199
iterations = 0
for i in range(0, 99):
    print(str(x)+'x'+str(x)+'>'+str(x-2)+'x'+str(x-2))
    x = x -2
    iterations = iterations + 1
print(iterations)
```

## 4. How are kernels initialized? 
**Ans**: The process of training a neural net involves randomly initializing kernals. The idea of random initialization is required to achieve the global minima - point 
where we get minimum loss - as early as possible. If we were to change kernal values sequentially, we might take a lot of time to achive required result.
This is because we might be at far end of spectrum and global minima values of kernals might be at the other end. Hence, random initialization is done to suit stochastic gradient descent
algorithm that is used to find the global minima - least loss point of network.

## 5. What happens during the training of a DNN?
**Ans**: A DNN is made up of many layers containing neurons. The example here is of a 4 layered network. All layers have a specific role to play in training process.
First layer extracts edges and gradients of image. Next layer 
extracts textures and patters from image. Post that parts of objects and objects are made out in next layers of network. 
During training, the kernals are initialized to random values and are asked to extract/filter specific features from image. In the output layer of network, a loss function is
computed that shows how predicted output is deviating from actual output. The loss function is propagated back to the previous layers using which the value of kernals are adjusted. 
The aim of this adjustment is to make sure we have low loss values during the next iteration of training process.
