def cal(arr):
    if arr.shape != (9,):
        print("The list must contain nine numbers.")
        return
    arr = arr.reshape(3,3)
    mean = [None]*3
    std= [None]*3
    var= [None]*3
    max_= [None]*3
    min_= [None]*3
    sum_ = [None]*3
    mean[0] = arr.mean(axis = 0).tolist()
    mean[1] = arr.mean(axis = 1).tolist()
    std[0] = arr.std(axis = 0).tolist()
    std[1] = arr.std(axis = 1).tolist()
    var[0] = arr.var(axis = 0).tolist()
    var[1] = arr.var(axis = 1).tolist()
    max_[0] = arr.max(axis = 0).tolist()
    max_[1] = arr.max(axis = 1).tolist()
    min_[0] = arr.min(axis = 0).tolist()
    min_[1] = arr.min(axis = 1).tolist()
    sum_[0] = arr.sum(axis = 0).tolist()
    sum_[1] = arr.sum(axis = 1).tolist()
    arr = arr.reshape(9,)
    mean[2] = arr.mean()
    std[2] = arr.std()
    var[2] = arr.var()
    std[2] = arr.std()
    max_[2] = arr.max()
    min_[2] = arr.min()
    sum_[2] = arr.sum()
    obj = {}
    obj['mean'] = mean
    obj['variance'] = var
    obj['standard deviation'] = std
    obj['max'] = max_
    obj['min'] = min_
    obj['sum'] = sum_
    return obj
