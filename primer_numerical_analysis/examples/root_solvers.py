"""Exercise the actual published scalar root solvers, including failures."""
from pathlib import Path

source = Path('primer_numerical_analysis.md').read_text()
section = source.split('### Shared Example: Find Root', 1)[1]
code = section.split('```python\n', 1)[1].split('\n```', 1)[0]
namespace = {}
exec(compile(code, 'published root solvers', 'exec'), namespace)
bisect, newton = namespace['bisection'], namespace['newton']
assert bisect(lambda x: x, 0., 1.) == 0.
assert bisect(lambda x: x - 1, 0., 1.) == 1.
assert abs(bisect(lambda x: 1e-20 * (x - .3), 0., 1.) - .3) < 1e-12
assert abs(newton(lambda x: x*x-2, lambda x: 2*x, 1.)**2-2) < 1e-12
assert newton(lambda x: x*x, lambda x: 2*x, 0.) == 0.
for call in [lambda: bisect(lambda x: x*x-2, 0., 2., max_iter=1),
             lambda: newton(lambda x: x*x-2, lambda x: 2*x, 1., max_iter=1),
             lambda: bisect(lambda x: x*x+1, 0., 2.),
             lambda: bisect(lambda x: float('nan'), 0., 1.),
             lambda: newton(lambda x: x+1, lambda x: 0., 0.)]:
    try: call()
    except (ValueError, RuntimeError): pass
    else: raise AssertionError('expected solver failure')
