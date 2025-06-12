import params
import evaluator
from perf_counter import PerfCounter


def custom_workload(
    poly_ctxt: params.PolyContext,
    scheme_params: params.SchemeParams,
):
    """
    A custom workload that performs a series of CKKS operations
    """
    stats = PerfCounter()
    
    # Let's assume our program is a*b + c*d for fresh ctxts
    # The simulator does not really care about the actual values, 
    # just their sizes/etc, which is what poly_ctxt contains
    
    # a*b
    evaluator.multiply(poly_ctxt, scheme_params.arch_param)
    # c*d
    evaluator.multiply(poly_ctxt, scheme_params.arch_param)
    
    # Now we need to run an addition, but we know we're one level down:
    post_mul_poly_ctxt = poly_ctxt.drop()
    evaluator.add(post_mul_poly_ctxt,scheme_params.arch_param)
       
    return stats