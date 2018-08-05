"""
    主函数
    variable：河南，湖北，湖南，江西

    domain：河南：[红绿蓝白]，湖北：[红绿蓝白]，湖南：[红绿蓝白]，江西：[红绿蓝白]

    condition：区域两两不能同色
            不同色(河南，湖北)，不同色(湖北，湖南)，不同色(湖北，江西)，不同色(湖南，江西)
    问题描述矩阵(tsp参数)：
            河南 湖北 湖南 江西
                   0 1 2 3 
                 0 x              
                 1 1 x
                 2 0 1 x
                 3 0 1 1 x
    实际地图上河南和湖北挨着，湖北湖南挨着，湖北江西挨着，湖南江西挨着
    domain参数为颜色，例如 当前河南是红色，那么domain的值应该是
        [['R'],['B', 'G'],['B', 'G', 'R'],['B', 'G', 'R']]
"""
import numpy as np
from model import backTrack

if __name__ == '__main__':
    # 定义问题描述
    csp_describe = np.array([[0], [1, 0], [0, 1, 0], [0, 1, 1, 0]])
    assign0 = dict({0: 'R'})
    dom0 = [['R'], ['B', 'G'], ['B', 'G', 'R'], ['B', 'G', 'R']]
    result0 = backTrack(assign0, csp_describe, dom0)
