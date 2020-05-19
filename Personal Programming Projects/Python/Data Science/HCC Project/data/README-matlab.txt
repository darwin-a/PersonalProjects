% HCC DATA STRUCTURE
%
%   'data' is a struct with the following fields:
%           .A = matrix of data (including class target in the last column)
%           .X = matrix of data (only features)
%           .Y = class target vector
%           .CatLogical = 1/0 logical vector identifying categorical (1) and continuous (0) features
%           .Labels = original labels of each categorical feature
%	    .nomspec = original labels of each categorical feature (similar to Labels, but specifying their names)
%           .varNames = feature names
%           .name = dataset name

         

Additional information:

Missing Values are denoted as 'NaN'.

Categorical values are processed to double. As an example, consider a categorical feature 'Color' that assumes "Red, Blue, Green". These values will be transformed to 1, 2, 3 but they should be treated as nominal values during the machine learning experiments (.CatLogical contains this information). However, if it is necessary to write back to "Red, Blue, Green", the structure data.nomspec has the original unique values so that this conversion is possible. For instance, data.nomspec.Color would return a 3×1 cell array: 

    'Red'
    'Blue'
    'Green'


Citation request:
Miriam Seoane Santos, Pedro Henriques Abreu, Pedro J Garcia-Laencina, Adelia Simao, Armando Carvalho, A new cluster-based oversampling method for improving survival prediction of hepatocellular carcinoma patients, Journal of biomedical informatics, 58, 49-59, 2015.