import sys
from DDEParams import DDEParams
from DDEval import DDEval


if __name__ == '__main__':
    params = DDEParams()
    params.validate_params(sys.argv[1:])
    # print(params)

    if params.is_valid:
        dd_eval = DDEval(params)
        dd_eval.parse()
    else:
        print('invalid params')

