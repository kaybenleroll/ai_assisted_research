# Complex Analysis: A Technical Primer

Complex analysis looks like a narrow extension of calculus until its central fact becomes visible: requiring a derivative to be independent of direction forces an extraordinary amount of structure. Holomorphic functions are rigid, contour integrals encode local singularities, and geometric maps turn difficult boundary problems into simpler ones. This primer develops that chain with enough theory to use it, enough geometry to see it, and enough computation to test your understanding without confusing a numerical picture for a proof.


## 1. Orientation, prerequisites, and complex-plane geometry

### Why a second plane changes calculus

A real differentiable function can behave almost arbitrarily away from the point where you differentiate it. A complex differentiable function has much less freedom. Once it has a complex derivative throughout an open region, its values on a small circle determine every value inside that circle. It has derivatives of every order and a convergent power series nearby. Contour integrals then connect local behavior at singularities to global quantities such as definite integrals and zero counts. This is the useful surprise of complex analysis: a stronger definition of derivative produces stronger tools.

This primer develops that chain of ideas for readers who know calculus and linear algebra. You will learn to recognize holomorphic functions, use Cauchy's formula, classify isolated singularities, evaluate residues, count zeros, and understand what conformal maps preserve. Later sections can turn this theory into boundary-value models and computational practice. This is not a full real-analysis text or a treatment of several complex variables. We will prove the transitions that explain the subject and mark the few foundational results whose complete proofs would require a longer detour.

The real-analysis facts needed here are manageable. A limit $z_n\to z$ means $|z_n-z|\to0$; a complex limit exists only if every way of approaching the point gives the same answer. A series converges absolutely when the series of moduli converges. Convergence is *uniform* on a set $E$ when one index works for every point of $E$ at once: for every $\varepsilon>0$ there is $N$ such that $|f_n(z)-f(z)|<\varepsilon$ for all $n\ge N$ and all $z\in E$. This stronger condition licenses passing a limit through an integral along a fixed finite-length contour, because
$$
\left|\int_\gamma (f_n-f)(z)\,dz\right|
\le \operatorname{length}(\gamma)\sup_{z\in\gamma}|f_n(z)-f(z)|\longrightarrow0.
$$
It does not automatically license differentiation of arbitrary series; power series receive a separate argument in Section 4. A set is *compact* in the plane if it is closed and bounded. A continuous function attains its maximum modulus on a compact set. More subtly, a compact set lying inside an open domain has positive distance from the domain's complement. That spare room lets us draw small circles around its points without leaving the domain. We will repeatedly work on a smaller closed disk or annulus inside a larger open one for exactly this reason.

If this is your first encounter with analysis language, keep four practical tests in view. To disprove a proposed limit, find two approaches that give different answers. To prove a limit, bound the modulus of the difference from the proposed value by something that tends to zero independently of direction. To exchange a limiting series with a contour integral, establish uniform convergence on the contour. To apply a theorem on a closed contour, check that the function is defined on an open neighborhood of the contour, not only at the boundary points you happen to sample. These tests will do more work than memorising a long list of theorems.

For instance, $\overline z/z$ has no limit as $z\to0$ through nonzero points. Along the real axis it equals $1$; along the imaginary axis it equals $-1$. In contrast, $|z|^2/z=\overline z$ tends to zero, since its modulus is $|z|$. The distinction matters when you inspect an apparent singularity: a formula that looks like $0/0$ may have a removable limit, a directional mismatch, or genuinely wild behavior. Algebraic appearance alone does not classify it.

Uniform convergence often comes from the *Weierstrass M-test*. If functions $g_n$ on $E$ satisfy $|g_n(z)|\le M_n$ for all $z\in E$, and the ordinary numerical series $\sum M_n$ converges, then $\sum g_n$ converges uniformly on $E$. On $|z|\le r<1$, the series $\sum_{n\ge0}z^n$ is controlled by $\sum r^n$ and is uniform. On the entire open disk $|z|<1$, the same simple bound fails because points can approach the boundary as $n$ grows. The sum still exists at every point in that disk, but the distinction between pointwise and uniform convergence explains why our later proofs always choose $r<R$ rather than work right up against the largest circle.

### Limits, compactness, and the spare room in a proof

The distinction between a limit at each point and a limit uniform over a whole set will recur throughout the subject. Consider $f_n(z)=z^n$ on the real interval $[0,1]$. At every $x<1$, $x^n\to0$, while $f_n(1)=1$. The pointwise limit is discontinuous, even though every $f_n$ is continuous. The convergence cannot be uniform: if it were, the uniform limit of continuous functions would be continuous. More directly, $\sup_{0\le x<1}x^n=1$ for every $n$. On $[0,r]$ with $r<1$, the same sequence converges uniformly because the supremum is $r^n$. Complex analysis repeatedly makes this smaller-set move: work on a closed disk strictly inside a domain, obtain a uniform bound there, and only then take a limit or differentiate a series.

Why does a uniform limit of continuous functions remain continuous? Fix a point $a$ and choose one approximant $f_N$ uniformly within $\varepsilon/3$ of the limit $f$. Continuity of that *single* $f_N$ gives a neighborhood where $|f_N(z)-f_N(a)|<\varepsilon/3$. The triangle inequality then bounds $|f(z)-f(a)|$ by three errors, each below $\varepsilon/3$. Pointwise convergence cannot supply one $N$ that works for all nearby $z$. This elementary three-term argument is the model for many later proofs: one finite approximant handles local geometry, and a uniform bound controls both ends of the comparison.

Uniform convergence on a contour is different from uniform convergence throughout its interior. In Cauchy's formula we need to interchange a series with an integral over one fixed circle, so a uniform bound on that circle suffices. To show a series represents a holomorphic function on an open disk, we want uniform convergence on every *compact subdisk*. This is called local uniform convergence. It does not demand one bound that works all the way out to the boundary. For the geometric series $\sum z^n$, every $|z|\le r<1$ works, while no single geometric majorant works over all $|z|<1$. The natural convergence notion follows the geometry of the proof, not a preference for a stronger theorem.

There is a second real-analysis distinction behind contour arguments: a small function value at some distant points does not control an integral along a growing path. Let $\gamma_R$ have length $L_R$ and suppose $|f|\le M_R$ on it. The useful estimate is $|\int_{\gamma_R}f\,dz|\le M_RL_R$. If $M_R\to0$ but $M_RL_R$ does not, the integral need not vanish. For example, $1/z$ has size $1/R$ on the circle $|z|=R$, whose length is $2\pi R$; its integral remains $2\pi i$ for every $R$. This is a good diagnostic before you start a large-semicircle residue calculation: record both the size of the integrand and the length of the added path.

Compactness supplies the missing margins in these estimates. Suppose $K$ is compact and contained in an open set $D$. For each $z\in K$ there is a disk around $z$ lying in $D$. A finite subcover gives a uniform positive radius small enough for local arguments around every point of $K$. Equivalently, $\operatorname{dist}(K,\mathbb C\setminus D)>0$ when the complement is nonempty. This is why the phrase “$f$ is holomorphic near the closed disk” is stronger than “$f$ is holomorphic in the open disk”: the former gives room to choose an enclosing circle and a bound on it. If a singularity sits on the proposed boundary, shrinking the circle may repair the argument; simply evaluating the formula at boundary sample points does not.

Absolute convergence is another practical guardrail. If $\sum |a_n|<\infty$, rearranging terms cannot change $\sum a_n$, and the tails have a numerical bound independent of order. Conditional convergence lacks that freedom. Laurent series separate positive and negative powers, and both tails converge absolutely on compact subannuli. That is why we can integrate or differentiate those tails term by term there. A formal expression with both positive and negative powers is not enough: you need an annulus where both tails actually converge.

Finally, keep the different meanings of “smooth” separate. The function $z\mapsto |z|^2=x^2+y^2$ is infinitely differentiable as a function of two real variables, but it is not holomorphic on any open disk. The real smooth function
$$
h(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0\end{cases}
$$
has every derivative at zero equal to zero, yet its Taylor series there is identically zero and does not recover the function away from zero. Complex holomorphy prevents that behavior: Cauchy's formula proves that the Taylor series actually equals the function nearby. The implication is not a matter of notation; the requirement that the same derivative exist from every complex direction gives a contour identity that ordinary real smoothness does not provide.

### Arithmetic is geometry

Write $z=x+iy$, where $x,y\in\mathbb R$ and $i^2=-1$. Conjugation reflects across the real axis: $\overline z=x-iy$. The modulus is distance from the origin, $|z|=\sqrt{x^2+y^2}$, and $z\overline z=|z|^2$. For $z\ne0$,
$$
\frac1z=\frac{\overline z}{|z|^2},\qquad
z=r e^{i\theta}=r(\cos\theta+i\sin\theta),\qquad r=|z|>0.
$$
An *argument* $\theta$ is an angle for $z$, but it is determined only modulo $2\pi$. Multiplication multiplies moduli and adds arguments; dividing reverses those operations. Thus multiplication by $2e^{i\pi/3}$ doubles every distance from the origin and rotates by $60^\circ$. Addition by $a$ translates the plane. These are geometric statements about simple complex formulas, and they become a local description of every holomorphic map whose derivative is nonzero.

The $n$th roots of $w=R e^{i\phi}\ne0$ are
$$
z_k=R^{1/n}\exp\!\left(i\frac{\phi+2\pi k}{n}\right),
\qquad k=0,1,\ldots,n-1.
$$
For example, the cube roots of $-8=8e^{i\pi}$ are $2e^{i\pi/3}$, $-2$, and $2e^{5i\pi/3}$. They sit at equal angular intervals on the radius-$2$ circle. Choosing a different representative for $\phi$ permutes the list; it does not create new roots.

An open connected subset $D\subset\mathbb C$ is a *domain*. Open means each point has a small disk still inside $D$; connected means the region is in one piece. A disk and a half-plane have no holes. An annulus $r<|z|<R$ and the punctured plane $\mathbb C\setminus\{0\}$ do. More precisely, a planar domain is *simply connected* if every closed loop in it can be continuously contracted to a point while remaining in the domain. This distinction matters later: $1/z$ is complex differentiable at every point of the punctured plane, but its integral around the origin is $2\pi i$.

Several standard subsets occur so often that it helps to recognise their geometry from inequalities. The disk $|z-a|<R$ is the set of points within distance $R$ of $a$; $|z-a|=R$ is its positively oriented boundary when traversed counterclockwise. The upper half-plane is $\Im z>0$. A horizontal strip has $\alpha<\Im z<\beta$. The sector $\alpha<\arg z<\beta$, with an angle interval shorter than $2\pi$, excludes a ray or boundary rays and supports a continuous angle. You will meet disks when applying Cauchy's formula, half-planes when closing Fourier contours, and sectors when defining branches of powers.

The difference between a region and its boundary is not pedantry. The function $1/(z-1)$ is holomorphic on the disk $|z|<1$, but it blows up at the boundary point $1$. Cauchy's formula on the *unit circle* cannot be applied to it, because the integrand is not defined everywhere on that contour. Cauchy's formula on $|z|=r$ with any $r<1$ is perfectly valid. Whenever a proof says “choose a circle inside the domain,” it means the entire closed circle, and usually a little open collar around it, must fit.

There is another geometric operation worth learning before calculus: inversion. The map $z\mapsto1/z$ sends a large modulus to a small one, reverses argument, and is undefined at zero. A circle through zero generally maps to a straight line; a circle avoiding zero maps to another circle. The related map $z\mapsto1/\overline z$ is reflection across the unit circle: a point $re^{i\theta}$ goes to $r^{-1}e^{i\theta}$. Unlike $1/z$, this reflection uses conjugation and is not holomorphic. Keeping those two inversions apart prevents an easy geometric mistake when we reach Möbius transformations.

One early picture is worth keeping in mind. A domain-coloring plot assigns hue to $\arg f(z)$ and brightness or bands to $|f(z)|$. For $f(z)=z^2$, a small counterclockwise circle around zero makes the hue cycle twice. That twofold *phase winding* is the zero's multiplicity, which we will recover without a plot using the argument principle. At the origin itself, the phase is undefined; any color placed there is a display convention. A plot can reveal a pattern and suggest a contour, but pixels cannot establish a zero count or prove continuity across a suspected branch cut.

You can predict several pictures before drawing them. Under $z\mapsto z^2$, a ray at angle $\theta$ maps to a ray at $2\theta$ while its radius is squared. The first quadrant maps onto the upper half-plane, and a small circle around zero wraps around its image twice. Under $z\mapsto1/z$, circles of radius $r$ become circles of radius $1/r$ with orientation reversed if you follow the angle parameter through the map. Under $z\mapsto e^z$, vertical translation by $2\pi i$ repeats the same values. Domain coloring makes these rules visible, but the algebra tells you which features are structural and which are artifacts of sampling or a hue discontinuity.

## 2. Complex functions and analyticity

### The derivative must ignore direction

For $f:D\to\mathbb C$, continuity and limits use the modulus just as they do for functions $\mathbb R^2\to\mathbb R^2$. Complex differentiability at $z_0\in D$ asks for the stronger limit
$$
f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h},
$$
where $h$ approaches zero through *every* complex direction. We call $f$ *holomorphic* on $D$ if it is complex differentiable at every point of $D$. Some authors use *analytic* as a synonym; the power-series theorem will later justify that terminology. Differentiability at one isolated point is a much weaker claim than holomorphy on a neighborhood.

Write $f(x+iy)=u(x,y)+iv(x,y)$. If $f'(z_0)$ exists, approach with real increments $h=t$ and imaginary increments $h=it$. Provided the relevant real partial derivatives are defined, the two computations give
$$
f'(z_0)=u_x+iv_x
=\frac{u_y+iv_y}{i}=v_y-iu_y.
$$
Equating real and imaginary parts yields the *Cauchy–Riemann equations*
$$
u_x=v_y,\qquad u_y=-v_x.
$$
These equations are necessary at a point where the complex derivative exists. A useful converse has an explicit regularity assumption: if $u$ and $v$ have continuous first partial derivatives on an open neighborhood and satisfy the equations there, then $f$ is holomorphic on that neighborhood. Real differentiability gives the linear increment
$$
f(z+h)-f(z)=(u_x+iv_x)\Re h+(u_y+iv_y)\Im h+o(|h|).
$$
The equations make its first two terms equal $(u_x+iv_x)h$; dividing by $h$ then leaves an error tending to zero. Checking two directional derivatives at one point without the real differentiability hypothesis does not prove complex differentiability there. Even a genuine complex derivative at one point does not make a function holomorphic nearby: $f(z)=|z|^2$ has $f'(0)=0$, and its partial derivatives satisfy Cauchy–Riemann at $0$, but it is not holomorphic on any neighborhood of $0$.

For a quick negative test, $f(z)=\overline z$ gives $u=x$, $v=-y$, hence $u_x=1\ne-1=v_y$. Directly, $\overline h/h$ equals $1$ along the real axis and $-1$ along the imaginary axis. By contrast, $f(z)=z^2$ gives $u=x^2-y^2$ and $v=2xy$, so $u_x=v_y=2x$ and $u_y=-v_x=-2y$ everywhere. Its derivative is $2z$. The real Jacobian of a holomorphic function is therefore
$$
Df(z)=\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}
=\begin{pmatrix}a&-b\\b&a\end{pmatrix},\qquad f'(z)=a+ib.
$$
This matrix rotates and scales infinitesimal vectors by $f'(z)$; its determinant is $|f'(z)|^2$. At a point where $f'(z)\ne0$, the map preserves oriented angles locally. At a critical point such as $z=0$ for $z^2$, this first-order picture collapses.

The example $|z|^2$ deserves a second look because it exposes the difference between a derivative at a point and an open region of derivatives. With $f(z)=x^2+y^2$, its Cauchy–Riemann equations read $2x=0$ and $2y=0$, so they hold only at the origin. At that point
$$
\frac{f(h)-f(0)}{h}=\frac{|h|^2}{h}=\overline h\longrightarrow0.
$$
The derivative really exists at zero. Yet any disk around zero contains points at which the Cauchy–Riemann equations fail. We cannot invoke Cauchy's formula on such a disk, and no power series centered at zero represents $|z|^2$ on a neighborhood. Its ordinary two-variable smoothness, even with derivatives of every real order, does not replace holomorphy.

Here is a positive example where the equations help build a function rather than reject one. Let $u(x,y)=x^2-y^2$. We seek $v$ so that $u+iv$ is holomorphic. The equations give $v_y=u_x=2x$ and $v_x=-u_y=2y$. Integrating the first gives $v=2xy+C(x)$; differentiating in $x$ and comparing with $2y$ forces $C'(x)=0$. Thus $v=2xy+C$ and $f(z)=z^2+iC$. The arbitrary constant reflects that a harmonic conjugate is unique only up to an additive real constant on a connected domain. If the given $u$ had failed $\Delta u=0$, the equations would have been incompatible; harmonicity is the integrability condition for this construction.

### Exponential, logarithm, and what a branch chooses

The complex exponential is $e^{x+iy}=e^x(\cos y+i\sin y)$. It obeys the ordinary product rule $e^{z+w}=e^ze^w$ and derivative $(e^z)'=e^z$. But $e^{z+2\pi i}=e^z$, so it cannot have one inverse on all of $\mathbb C\setminus\{0\}$. Every logarithm of $z=re^{i\theta}$ has the form
$$
\log z=\ln r+i(\theta+2\pi k),\qquad k\in\mathbb Z.
$$
A *branch* picks one continuous angle on a suitable domain. The principal logarithm $\operatorname{Log}z=\ln|z|+i\operatorname{Arg}z$ takes $\operatorname{Arg}z\in(-\pi,\pi)$ and is holomorphic on $\mathbb C\setminus(-\infty,0]$, with derivative $1/z$. The removed negative real ray is a branch cut, a choice of domain for a single-valued formula. It is not a new singularity at every point of the ray: another branch can cross most of that ray by placing its cut elsewhere. No branch crosses all the way around zero, because a continuous argument would have to increase by $2\pi$ yet return to its starting value.

For a chosen logarithm branch $L$, define $z^\alpha=e^{\alpha L(z)}$. Changing $L$ by $2\pi i$ changes this value by $e^{2\pi i\alpha}$. Integer powers are therefore single-valued; noninteger powers usually depend on the branch. For the principal square root, $\sqrt{z}=e^{\operatorname{Log}z/2}$ on the slit plane. When you multiply such expressions, check that the same branch remains valid: $\operatorname{Log}(zw)$ need not equal $\operatorname{Log}z+\operatorname{Log}w$ because the two principal arguments may differ by $2\pi$.

An explicit discontinuity shows what the cut does. Approach the negative real point $-1$ from above: the principal argument tends to $\pi$, so $\operatorname{Log}z\to i\pi$. Approach it from below: the principal argument tends to $-\pi$, so $\operatorname{Log}z\to-i\pi$. The values differ by $2\pi i$. The function $1/z$ is perfectly regular near $-1$; the jump belongs to our chosen inverse of the exponential. If an application needs continuity across the negative real axis but never crosses the positive real axis, move the cut to the positive ray and use an argument interval such as $(0,2\pi)$ instead.

For complex $\alpha$, the branch choice can change not only phase but modulus: $|e^{2\pi i\alpha}|=e^{-2\pi\Im\alpha}$. This is why a complex power is not simply “the usual power with a complex input.” Its definition includes a domain and an angle convention. In later contour integrals involving $z^\alpha$, the two sides of a cut may carry genuinely different weights. The residue theorem applies only to regions where the chosen branch is single-valued and holomorphic; a keyhole contour keeps track of both sides of the removed ray.

Define $\sin z=(e^{iz}-e^{-iz})/(2i)$ and $\cos z=(e^{iz}+e^{-iz})/2$. They are holomorphic everywhere. Unlike real sine and cosine, they are unbounded in imaginary directions: $\sin(iy)=i\sinh y$. This matters when choosing a large contour; familiar real-axis bounds do not follow the function into the upper half-plane.

Their familiar identities survive because they come from the exponential laws: $\sin^2z+\cos^2z=1$ and $(\sin z)'=\cos z$. Their zero sets, however, are discrete points in the plane, not curves. A nonzero holomorphic function cannot vanish along an arc inside its domain without vanishing everywhere, as the identity theorem will make precise. Compare that with a real-valued function of two variables, whose zero set is often a curve. This is another way to feel how restrictive a single complex derivative is.

### Branches under continuation

The logarithm is best understood as a local inverse with a global obstruction. The exponential maps a horizontal strip of height $2\pi$ one-to-one onto a slit plane when its boundary lines are chosen consistently. On the strip $-\pi<\Im w<\pi$, its inverse is the principal logarithm on $\mathbb C\setminus(-\infty,0]$. The derivative follows from the inverse-function calculation: if $e^{L(z)}=z$, then $e^{L(z)}L'(z)=1$, so $L'(z)=1/z$. The same derivative appears on every logarithm branch. Derivatives cannot distinguish two branches that differ by a constant $2\pi ik$; the value at one base point fixes which branch you mean.

Here is a useful test for whether a domain can carry a logarithm. A holomorphic logarithm of $z$ on $D\subset\mathbb C\setminus\{0\}$ implies that $1/z$ has a primitive on $D$, so every closed contour in $D$ has integral zero. Conversely, if $1/z$ has a primitive $F$ on a connected $D$, then $(e^{-F(z)}z)'=0$. Thus $e^{-F(z)}z$ is a nonzero constant; adding a suitable constant to $F$ gives $e^{L(z)}=z$. The equivalence turns an inverse-function question into a period question. A slit plane passes this test. The punctured plane fails because its unit circle has integral $2\pi i$ of $1/z$. Simple connectedness is a convenient sufficient condition for a nonvanishing holomorphic function to admit a holomorphic logarithm, but the actual obstruction is the nonzero winding of its image around zero.

The familiar identity $\operatorname{Log}(zw)=\operatorname{Log}z+\operatorname{Log}w$ fails in an instructive way. Take $z=w=e^{3\pi i/4}$. Both principal arguments are $3\pi/4$, so their principal logarithms add to $3\pi i/2$. Their product is $e^{3\pi i/2}=-i$, whose principal argument is $-\pi/2$. Thus $\operatorname{Log}(zw)=-\pi i/2$, differing by $2\pi i$. Exponentiating either answer gives the same product. The algebraic law has not disappeared; it holds modulo the period of the exponential. The same correction appears in products of complex powers, where it may matter after exponentiation by a noninteger $\alpha$.

For the principal square root, write $z=re^{i\theta}$ with $-\pi<\theta<\pi$. Then $\sqrt z=\sqrt r\,e^{i\theta/2}$ has positive real part throughout the slit plane. Crossing the negative axis changes the limiting sign: just above $-r$ the root tends to $i\sqrt r$, just below it tends to $-i\sqrt r$. A loop around zero therefore exchanges the two local square-root values. You cannot repair that exchange by placing a clever cut that still lets the loop close inside the domain. In contrast, on a small disk avoiding zero, choose an angle interval and the square root is an ordinary holomorphic function.

Branch points and poles behave differently under analytic continuation. Continue $1/(z-a)$ around $a$: its value returns unchanged, even though its contour integral may be nonzero. Continue a local $\sqrt z$ around zero: the value changes sign. A pole is an isolated singularity of a single-valued function; a branch point prevents a single-valued branch on any full punctured disk around it. This distinction matters before invoking Laurent's theorem. A Laurent series with integer powers is valid on a full annulus where the function is single-valued and holomorphic. A square root on a slit annulus has a branch, but the slit prevents the domain from being the full annulus required by that theorem.

The inverse trigonometric functions inherit the same issue. To solve $\sin w=z$, set $q=e^{iw}$. Then $2iz=q-q^{-1}$, hence $q^2-2izq-1=0$ and
$$
q=iz\pm\sqrt{1-z^2},\qquad
w=-i\log q.
$$
This formula contains both a square root and a logarithm, so “$\arcsin z$” needs branch choices before it becomes a holomorphic function. Differentiating a chosen local inverse gives $(\arcsin z)'=1/\sqrt{1-z^2}$ wherever the chosen branch is regular. The points $z=\pm1$ are where the inverse derivative becomes singular; a domain and cuts determine which other points are excluded for single-valuedness. If a calculation substitutes the real inverse-sine identity into a complex contour, check these choices before treating the derivative formula as global.

There is a similar but simpler lesson in the exponential's geometry. The map $e^z$ never vanishes, and $|e^{x+iy}|=e^x$. Vertical lines map to circles about zero; horizontal lines map to rays. A rectangle of width $A$ and height less than $2\pi$ maps to an annular sector without overlap, provided its horizontal edges do not cross the same argument. Increasing its height past $2\pi$ makes images overlap, even though $(e^z)'$ never vanishes. Local invertibility follows from the nonzero derivative; global invertibility requires control of the domain. This is an early concrete model for the local-versus-global distinction in conformal mapping.

The hyperbolic functions also help check growth claims. From $\cos z=\cos x\cosh y-i\sin x\sinh y$ one obtains
$$
|\cos(x+iy)|^2=\cos^2x+\sinh^2y.
$$
Thus $|\cos z|$ generally grows exponentially as $|\Im z|$ grows, even when $|\cos x|\le1$ on the real axis. The real-axis estimate is useless on a tall rectangular contour. The formula also shows that a zero of cosine needs $y=0$ and $\cos x=0$, so its zeros occur at the familiar real points $\pi/2+k\pi$. Growth and zero location follow from the same elementary decomposition. It is good practice to calculate the modulus in the actual region where a proposed contour travels.

Complex powers offer a sharper branch diagnostic than square roots. Let $z^\alpha=e^{\alpha L(z)}$ for a chosen logarithm $L$. Continue the local branch once counterclockwise around zero. The logarithm increases by $2\pi i$, so the power is multiplied by $e^{2\pi i\alpha}$. If $\alpha=p/q$ is a rational number in lowest terms, $q$ circuits return to the starting value; the local branches form a finite cycle. If $\alpha$ is irrational real, no positive number of circuits restores the initial value. If $\Im\alpha\ne0$, each circuit also rescales the modulus by $e^{-2\pi\Im\alpha}$. These are different kinds of monodromy—the change produced by analytic continuation around a loop—and they explain why branch bookkeeping can affect both phase and magnitude.

For a concrete cut calculation, take the principal branch $z^{1/3}=e^{\operatorname{Log}z/3}$. At $-r$ approached from above, its value tends to $r^{1/3}e^{i\pi/3}$; from below it tends to $r^{1/3}e^{-i\pi/3}$. Those limiting values are different cube roots of the same negative number. Neither is “wrong.” The ambiguity is in the inverse operation, and a specified branch makes the function single-valued only on its chosen domain. If you integrate a function containing $z^{1/3}$ around a keyhole contour, keep the two boundary values separate. They are related by a known phase factor, not equal terms that cancel automatically.

### Harmonic functions and their conjugates

Suppose $f=u+iv$ is holomorphic. The power-series result to come ensures its components have continuous second derivatives. Differentiate the Cauchy–Riemann equations and use equality of mixed partials:
$$
\Delta u=u_{xx}+u_{yy}=v_{yx}-v_{xy}=0,
\qquad \Delta v=0.
$$
A real-valued function satisfying $\Delta u=0$ is *harmonic*. Conversely, if $u$ is harmonic on a disk, the one-form $-u_y\,dx+u_x\,dy$ is closed; the planar potential theorem on a disk gives a function $v$ with $v_x=-u_y$ and $v_y=u_x$. Then $u+iv$ is holomorphic. The same construction works locally on any domain. Global single-valuedness can fail when loops encircle a hole.

The clean example is $u(z)=\ln|z|$ on $\mathbb C\setminus\{0\}$. It is harmonic there, and its local harmonic conjugate is $\arg z$. The required differential is
$$
dv=-u_y\,dx+u_x\,dy
=\frac{-y\,dx+x\,dy}{x^2+y^2}.
$$
Integrating this form once around $|z|=1$ gives $2\pi$, so no globally single-valued $v$ exists on the punctured plane. On a slit plane, $v=\operatorname{Arg}z$ works. This is the same obstruction that prevents a global logarithm and makes $\int dz/z$ nonzero around the origin. One topology issue appears in three languages: harmonic conjugates, inverse exponentials, and contour integrals.

There is a useful direction to the correspondence. If you can identify a holomorphic $f=u+iv$, you get two harmonic functions at once. Conversely, solving $\Delta u=0$ in a region gives a local route to a holomorphic function, which can simplify a potential or flow problem. But a harmonic function by itself does not specify the conjugate's global behavior or boundary conditions. Even on a simply connected region, adding a constant to $v$ changes no derivatives; on a multiply connected region, periods around holes can prevent a single-valued $v$ altogether. When applying this to physics, one must also check what $u$ and $v$ represent and what assumptions make a potential description valid.

## 3. Contours and Cauchy theory

### Integrating along a directed curve

A *contour* $\gamma:[a,b]\to D$ is a directed curve made of finitely many continuously differentiable pieces. Reversing its direction changes the sign of an integral. The complex contour integral is defined by parametrisation:
$$
\int_\gamma f(z)\,dz
=\int_a^b f(\gamma(t))\gamma'(t)\,dt.
$$
Different regular parametrisations with the same orientation give the same value. For the counterclockwise circle $\gamma(t)=a+re^{it}$, $0\le t\le2\pi$, we have $dz=ire^{it}\,dt$. A first calculation therefore needs no theorem:
$$
\int_{|z-a|=r}\frac{dz}{z-a}
=\int_0^{2\pi}\frac{ire^{it}}{re^{it}}\,dt=2\pi i.
$$
Parametrisation also tells you when a familiar-looking line integral is *not* a candidate for Cauchy's theorem. On $|z|=r$ counterclockwise, $\overline z=re^{-it}$ and $dz=ire^{it}\,dt$, so
$$
\int_{|z|=r}\overline z\,dz
=\int_0^{2\pi} ir^2\,dt=2\pi i r^2.
$$
The curve encloses no singularity of the continuous function $\overline z$, yet the integral is nonzero. Cauchy's theorem requires holomorphy, not merely continuity or the absence of an obvious pole. The value also changes with the radius, unlike $\int dz/z$. This direct contrast separates two reasons for a nonzero closed integral: the integrand may fail to be holomorphic inside, or the domain may have a hole containing a singularity.

Along a straight segment from $p$ to $q$, take $\gamma(t)=p+t(q-p)$, $0\le t\le1$. Then
$$
\int_{[p,q]}f(z)\,dz
=(q-p)\int_0^1 f(p+t(q-p))\,dt.
$$
For $f(z)=z$, this gives $(q^2-p^2)/2$ no matter which path you choose, because $z$ has primitive $z^2/2$. For $f(z)=\overline z$, take $p=0$ and $q=1+i$: the straight segment gives $\overline q q/2=1$, while the two-segment path $0\to1\to1+i$ gives $1+i$. Path dependence is not an abstract pathology; it appears in the simplest non-holomorphic example.

An upper bound is often as useful as an exact value. If $|f(z)|\le M$ along $\gamma$ and its length is $L$, the *ML estimate* gives
$$
\left|\int_\gamma f(z)\,dz\right|\le ML.
$$
The estimate follows by applying the triangle inequality to the parametrised integral. It is the standard way to show that an extra arc disappears in a contour argument; one must bound both the integrand and the arc length. A statement that a function “decays at infinity” is insufficient if the contour length grows faster.

For a closed contour avoiding $a$, define its *winding number* about $a$ by
$$
\operatorname{Ind}(\gamma,a)
=\frac{1}{2\pi i}\int_\gamma\frac{dz}{z-a}.
$$
It counts net counterclockwise turns and is an integer. One way to see the integer is to follow a continuous argument of $\gamma(t)-a$ along the parameter interval: the final angle differs from the initial angle by a multiple of $2\pi$. A simple counterclockwise Jordan curve has index $1$ at interior points and $0$ outside; clockwise orientation gives $-1$. The index formulation will later let us speak about contours more general than a single simple boundary.

The index is stable as long as a contour moves without crossing $a$. Imagine pulling a rubber band around a nail: deformation changes its shape but not the number of wraps. If the band crosses the nail, the index may change. This intuition becomes rigorous through contour deformation, but it already tells you why “moving the contour” always needs a singularity check. It also tells you why the residue theorem sums only the poles inside the chosen path. A contour integral is sensitive to how its path sits relative to excluded points, not just to the formulas at its endpoints.

### Winding is a directed count

The winding number has two descriptions that should agree in any calculation. One is the integral of $1/(z-a)$. The other is the net change of a continuously tracked angle along the curve, divided by $2\pi$. To see the link, suppose $\gamma(t)-a=\rho(t)e^{i\theta(t)}$ along a closed piecewise smooth contour, with $\rho(t)>0$ and a continuously *unwrapped* angle $\theta(t)$. On each smooth piece,
$$
\frac{\gamma'(t)}{\gamma(t)-a}
=\frac{\rho'(t)}{\rho(t)}+i\theta'(t).
$$
The real term integrates to $\log\rho(b)-\log\rho(a)=0$, because the path closes. The imaginary term integrates to $i[\theta(b)-\theta(a)]$. Although the final point equals the initial point, the unwrapped angle may differ by $2\pi k$. The integral is therefore $2\pi ik$. This derivation also explains why the index is an integer without appealing to a diagram. Tracking principal arguments independently at sampled points would lose the integer whenever the phase jumps across its displayed cut.

Self-intersections do not invalidate winding number. Let $\gamma(t)=a+Re^{2it}$ for $0\le t\le2\pi$. Geometrically its trace is one circle, but the parametrisation traverses it twice. Its index about $a$ is $2$, not $1$. A figure-eight contour can have index $+1$ in one lobe, $-1$ in the other, and $0$ outside. The index belongs to the *directed path with multiplicity*, not to the set of pixels its trace occupies. That distinction later determines the weights in a residue sum for non-simple contours.

For a contour made of an outer boundary and holes, the orientation of each component follows from keeping the region on your left as you travel. The outer boundary then runs counterclockwise; the boundary of each hole runs clockwise. Consider an annulus $r<|z|<R$ and $f(z)=1/z$. On its oriented boundary,
$$
\int_{|z|=R}^{\mathrm{ccw}}\frac{dz}{z}
+\int_{|z|=r}^{\mathrm{cw}}\frac{dz}{z}
=2\pi i-2\pi i=0.
$$
The function is holomorphic throughout the annulus, exactly as Cauchy–Goursat requires. Yet either component alone has a nonzero integral. The apparent contradiction disappears when you integrate over the complete boundary of the region on which the theorem is applied. This example is a reliable sign check for excision arguments.

Sometimes a contour is closed only after adding a segment or arc, and the added piece changes the integral. For a rectangle with vertices $0,1,1+i,i$, the boundary is counterclockwise in that order. If a complex integral along its bottom edge is the quantity you want, the other three edges must be bounded or computed; the closed integral does not equal the bottom-edge integral by definition. Likewise, a real interval $[-R,R]$ traversed left to right becomes a counterclockwise upper-half-plane contour when the semicircle runs from $R$ back to $-R$. This elementary orientation sketch prevents a surprising number of sign errors in residue calculations.

Contour deformation needs a region, not merely two endpoints. Suppose $f$ is holomorphic on and between two circles centered at $a$, with radii $r<R$. The annular theorem says their counterclockwise integrals agree. You may deform one to the other because the swept annulus contains no singularity. But if a pole lies between them, the difference is $2\pi i$ times its residue. For $f(z)=1/(z-1)$, circles centered at zero with radii $1/2$ and $2$ give $0$ and $2\pi i$. The pole at $1$ lies in the swept region. “Move the contour outward” is therefore an operation with a ledger: record every singularity crossed and its orientation.

The topology is visible even without a meromorphic singularity. A branch of $\log z$ is holomorphic on its slit domain, but a proposed deformation that crosses its cut is not a deformation *within that domain*. You may move the cut or choose another branch and re-express the integrand, but the two sides can carry different values of a complex power. If a contour surrounds a branch point, a keyhole construction follows the sides of the cut as separate directed paths. Treating them as one canceled segment silently assumes the integrand has equal boundary values there, which is exactly what the branch often denies.

The index is locally constant as a function of the reference point $a$ away from the contour. One way to see this is to choose $a$ and $b$ so close that $|a-b|<\min_{z\in\gamma}|z-a|$. Then the paths $\gamma(t)-a$ and $\gamma(t)-b$ can be connected by straight segments without passing through zero. Their winding numbers agree. Since an integer cannot vary continuously except by jumping, the index changes only when the reference point crosses the trace of the contour. For a simple Jordan curve this gives the familiar inside value $1$ and outside value $0$ after choosing positive orientation. For a multiply traced curve there may be regions with index $2$ or $-1$; the same local-constancy argument still applies.

This gives a practical method for checking a proposed residue sum. Mark the singularities and ask which connected component of the complement of the contour contains each one. A slight movement of a pole within its component cannot change its index weight. If an answer changes under such a movement while no pole crosses the path, either the proposed formula or the chosen contour is wrong. The principle is topological, but it works as a robust arithmetic check in ordinary calculations.

For piecewise smooth curves the bound $|\int_\gamma f\,dz|\le L\sup_\gamma|f|$ is immediate, but its use depends on finding a bound valid on *every* part of the path. Suppose $f(z)=1/(z^2+1)$ and the circle $|z|=R$ has $R>1$. The reverse triangle inequality gives $|z^2+1|\ge R^2-1$, so the full-circle integral is bounded in modulus by $2\pi R/(R^2-1)$. It tends to zero as $R\to\infty$. Indeed the residues at $i$ and $-i$ cancel. If the integrand were $z/(z^2+1)$, the analogous bound would be of order one, and the integral is actually $2\pi i$. The estimate detects when a limit is plausible; when it does not vanish, it does not prove the limit is nonzero, but it tells you more argument is needed.

There is one further subtlety in applying Cauchy–Goursat on a simply connected domain. The domain must be open, and the contour must remain inside it. A closed curve may touch the boundary of an open domain even when its interior is visually inside. At that contact point the integrand may be undefined or unbounded, so neither the integral nor a boundary version of the theorem follows. In practice, choose a smaller contour with positive clearance, prove the identity there, and then take a limit separately if the boundary is needed. The limiting step can introduce principal values or boundary terms; it is not part of the original theorem.

### Primitives, paths, and holes

If $F'=f$ throughout a domain and $\gamma$ runs from $p$ to $q$ within it, the chain rule gives
$$
\int_\gamma f(z)\,dz=F(q)-F(p).
$$
Thus an antiderivative, also called a *primitive*, makes the integral path independent and forces every closed-contour integral to vanish. Conversely, if all paths between two points have the same integral, fix $p$ and define $F(z)$ as the integral from $p$ to $z$. Integrating over a short final line segment and using continuity of $f$ shows $F'(z)=f(z)$. This converse requires a path-connected domain and integrable continuous $f$; domains in the plane are path connected.

For $f(z)=1/z$ on $\mathbb C\setminus\{0\}$, the unit-circle computation rules out a global primitive. There is no contradiction with the local primitive $\operatorname{Log}z$ on a slit plane. If a region has holes, a holomorphic function can have nonzero periods around them. Holomorphy alone settles the *local* calculus; topology decides whether that local calculus glues into a global primitive.

For a more precise local picture, fix a point $a\ne0$. A sufficiently small disk around $a$ avoids zero and admits a logarithm branch, so $1/z$ has a primitive on that disk. If you integrate around a loop lying entirely in such a disk, the result is zero. But a loop that surrounds the origin cannot fit into one logarithm chart whose branch returns to the same angle. You can cover the loop by many local charts, yet the angle increases by $2\pi$ after a full turn. That accumulated mismatch is the period $2\pi i$. It is the same phenomenon as a locally defined coordinate failing to be globally single-valued.

For a continuous $f$ on a simply connected domain, zero integrals around every closed contour imply path independence. The simply connected assumption is not logically needed for that equivalence; it is a convenient condition under which *holomorphy* guarantees the zero integrals. Keeping these statements distinct helps avoid circular reasoning: a primitive implies vanishing periods on any domain, while Cauchy–Goursat supplies vanishing periods from holomorphy when the loops can be filled inside the domain.

### Cauchy–Goursat and the subdivision idea

Here is a precise foundational version. If $T$ is a closed triangle and $f$ is holomorphic on an open neighborhood of $T$, then
$$
\int_{\partial T}f(z)\,dz=0
$$
for the counterclockwise boundary. The point of the Cauchy–Goursat theorem is that no continuity assumption on $f'$ is needed. A standard extension says: if $D$ is simply connected and $f$ is holomorphic on $D$, then its integral around every closed piecewise smooth contour in $D$ is zero. For a piecewise smooth simple closed contour one can instead assume that the contour and its bounded interior lie in the holomorphy domain. Do not omit that interior condition: the circle surrounding $0$ is not the boundary of a disk contained in $\mathbb C\setminus\{0\}$.

The triangle proof is a good model of why the derivative definition suffices. Subdivide $T$ into four similar triangles. Interior edges cancel, so at least one child has boundary integral whose modulus is at least one quarter of that of its parent. Choose such a child, subdivide again, and continue. The nested triangles shrink to a point $z_*$. Differentiability there gives
$$
f(z)=f(z_*)+f'(z_*)(z-z_*)+\varepsilon(z)(z-z_*),
\qquad \varepsilon(z)\to0\quad(z\to z_*).
$$
The constant and linear terms have zero integral around every triangle: they have primitives. On the $n$th triangle, the remaining term has modulus at most $\sup|\varepsilon|$ times its diameter. Its perimeter is proportional to the same diameter, so its integral is at most a constant times $\sup|\varepsilon|\,4^{-n}$. But our choices ensure the original integral is at most $4^n$ times the $n$th integral. Letting $n\to\infty$ forces the original integral to be zero. Extending from triangles to general contours uses subdivision or contour deformation; the topology hypotheses ensure that the needed filling stays in the domain.

What has this proof replaced? In a real-vector-calculus approach, one might write $f=u+iv$, convert $\int f\,dz$ into two real line integrals, and invoke Green's theorem with the Cauchy–Riemann equations. That works when $u$ and $v$ have sufficiently regular first partial derivatives on the filled region. Cauchy–Goursat needs only complex differentiability, so its conclusion is stronger than a proof that quietly assumes continuous derivatives. This is why the theorem is a genuine result, even if the Green's-theorem calculation provides an attractive first intuition.

The theorem also has a useful deformation corollary. If two simple closed contours wind around the same holes and the closed region between them contains no singularity of $f$, their integrals agree, provided $f$ is holomorphic on an open neighborhood of that intervening region and both boundaries. The annulus between two circles is the model case: its outer boundary is counterclockwise and its inner boundary clockwise, so the sum of boundary integrals is zero. We will use this annular equality to move Laurent coefficient circles and to shrink residue contours around poles. It does not say that either individual integral is zero; $1/z$ gives $2\pi i$ on every positively oriented circle around zero.

### Cauchy's formula: boundary values control the interior

Let $C$ be a positively oriented, piecewise smooth simple closed contour, let $a$ lie in its bounded interior, and suppose $f$ is holomorphic on an open neighborhood of the contour together with its closure of the interior. Then *Cauchy's integral formula* is
$$
f(a)=\frac{1}{2\pi i}\int_C\frac{f(z)}{z-a}\,dz.
$$
For the proof, remove a small closed disk about $a$ from the interior. The function $f(z)/(z-a)$ is holomorphic on a neighborhood of the remaining region, so its outer boundary integral equals the counterclockwise integral on the small circle $C_r$. On $C_r$, split $f(z)=f(a)+[f(z)-f(a)]$. The first term integrates to $2\pi i f(a)$. For the second, continuity gives
$$
\left|\int_{C_r}\frac{f(z)-f(a)}{z-a}\,dz\right|
\le 2\pi\max_{|z-a|=r}|f(z)-f(a)|\longrightarrow0.
$$
That limit proves the formula. The excision argument also shows why the orientation of the inner boundary is clockwise when it is viewed as part of the punctured region's boundary. If the point $a$ is outside $C$, the integrand is holomorphic on the entire interior and the integral is zero. If $a$ is on $C$, this formula is not applicable as stated.

There is a useful way to read the formula before doing any algebra. The function value at $a$ is an average of boundary values with the geometry encoded in $1/(z-a)$. A holomorphic function cannot be independently prescribed at a point after all its nearby boundary values have been fixed. This is a far stronger constraint than ordinary continuity. For a real differentiable function, knowing its values on a circle does not determine its values inside: you can add a smooth bump supported in the disk without altering the boundary. For a holomorphic function, such a bump would violate Cauchy's formula unless it were identically zero.

The formula also clarifies why the contour must be positively oriented. If you traverse the same $C$ clockwise, the integral changes sign, so the correct statement has a minus sign. With a contour that winds $k$ times around $a$ and otherwise meets suitable holomorphy conditions, the integral of $f(z)/(z-a)$ becomes $2\pi i k f(a)$. This index-weighted version and the simple-contour version express the same geometry; using the simple version first keeps the boundary and interior hypotheses visible.

For a concrete use, take $C:|z|=2$ counterclockwise. Since $e^z$ is entire and $1$ lies inside,
$$
\int_C\frac{e^z}{z-1}\,dz=2\pi i e.
$$
No parametrised integration of the exponential is required; the contour reads off the value at one interior point. Differentiating Cauchy's formula with respect to the interior point, justified because the denominator stays uniformly away from zero on $C$ while $a$ ranges over a smaller compact set, yields
$$
f^{(n)}(a)=\frac{n!}{2\pi i}
\int_C\frac{f(z)}{(z-a)^{n+1}}\,dz,\qquad n=0,1,2,\ldots.
$$
For a circle $|z-a|=R$ lying with its closed disk in the holomorphy domain, let $M_R=\max_{|z-a|=R}|f(z)|$. The ML estimate gives *Cauchy's estimates*
$$
|f^{(n)}(a)|\le\frac{n!M_R}{R^n}.
$$
As an example of the derivative formula, take $C:|z|=3$ and $a=1$. Since $e^z$ is holomorphic on and inside $C$,
$$
\int_C\frac{e^z}{(z-1)^3}\,dz
=\frac{2\pi i}{2!}\left.\frac{d^2}{dz^2}e^z\right|_{z=1}
=\pi i e.
$$
The denominator has a third-order pole, but this is still a Cauchy-formula calculation: the second derivative is what the cubic denominator extracts. In Section 5 the residue formula will recover exactly the same answer by identifying the coefficient of $(z-1)^{-1}$. Seeing both routes helps you choose the shorter one in a concrete calculation.

Several striking consequences are already visible. If $f$ is entire and bounded by a global $M$, let $R\to\infty$ with $n=1$: $f'(a)=0$ everywhere, so $f$ is constant (*Liouville's theorem*). If a nonconstant polynomial had no root, its reciprocal would be entire and bounded: outside a large disk the polynomial grows in modulus, while inside the disk the reciprocal has a finite maximum. Liouville then contradicts nonconstancy, proving the fundamental theorem of algebra. Section 4 draws a different consequence from the same formula: the function equals its Taylor series, not merely a finite Taylor approximation.

### How Cauchy's formula forces rigidity

Cauchy's formula is a reproducing rule. If you know $f$ on one admissible closed contour, the same integral kernel gives every value inside. The proof by removing a small disk is deceptively short; its key logical move is that the singularity of $1/(z-a)$ is *manufactured* at the point where we want to read off $f(a)$. The original $f$ has no singularity there. On the punctured region the product is holomorphic, so the outer integral equals the small-circle integral. Continuity makes the difference $f(z)-f(a)$ negligible on that circle, while the constant term contributes exactly $2\pi i f(a)$. You need no prior assumption that $f'$ is continuous, and for this first formula the small-circle estimate uses only continuity of $f$.

There is a small quantifier issue when differentiating the formula. Fix $a$ in the interior and let $d=\operatorname{dist}(a,C)>0$. If $w$ stays in $|w-a|<d/2$, then $|z-w|\ge d/2$ for $z\in C$. The difference quotients of $1/(z-w)$ converge uniformly on $C$, so the limit passes under the integral. Repeating this argument yields the higher derivative formula. The contour can remain fixed while the interior point moves in a compact subset. That uniform distance from the denominator's zero is what turns a formal differentiation into a valid proof.

For example, let $C$ be $|z|=2$ counterclockwise and consider
$$
I(a)=\frac{1}{2\pi i}\int_C\frac{\cos z}{z-a}\,dz,
\qquad |a|<2.
$$
The formula says $I(a)=\cos a$. Differentiation under the integral gives $I'(a)=(2\pi i)^{-1}\int_C\cos z/(z-a)^2\,dz=-\sin a$. At $a=0$ the integral with a squared denominator is zero. The result is not a symmetry guess about the circle; it follows from a family of identities valid throughout its interior. As $a$ approaches the boundary, the uniform denominator bound deteriorates. This proof does not automatically give a formula at $|a|=2$.

The Cauchy estimates say more than “all derivatives exist.” Suppose $f$ is holomorphic on a neighborhood of $|z-a|\le R$ and $|f|\le M$ on its boundary. Then $|f^{(n)}(a)|\le n!M/R^n$. If the disk radius doubles while the boundary bound stays comparable, high derivatives are strongly constrained. Conversely, a proposed holomorphic function with derivatives growing faster than this for every possible enclosing circle cannot exist on that disk. This is often a useful sanity check on a formal series. The estimate also proves that an entire function with polynomial growth is a polynomial: if $|f(z)|\le A(1+|z|)^m$ for all $z$ and an integer $m\ge0$, choose a large circle around zero. For $n>m$, Cauchy's estimate gives $|f^{(n)}(0)|\le n!A(1+R)^m/R^n\to0$ as $R\to\infty$. Hence all Taylor coefficients above degree $m$ vanish.

Another consequence is that zero values cannot accumulate inside a domain unless the whole function vanishes. Suppose $f$ has zeros $z_k\to a$ with $a$ interior. Continuity gives $f(a)=0$. If the Taylor series has a first nonzero term $c_m(z-a)^m$, then $f(z)=(z-a)^m g(z)$ with $g(a)=c_m\ne0$. The factor $g$ stays nonzero near $a$, so $a$ is the only zero in some disk, contradicting the accumulating zeros. Thus every Taylor coefficient vanishes and $f$ is zero near $a$; connectedness propagates the identity. This proof shows exactly why an accumulation at a boundary point does not trigger the theorem: there may be no admissible disk centered there.

The mean-value formula follows by using a circle centered at $a$. The factor $dz/(z-a)$ becomes $i\,d\theta$, giving
$$
f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+re^{i\theta})\,d\theta.
$$
Taking real parts shows that the real part of a holomorphic function has the same circular mean-value property. That is one route to the maximum principle for harmonic functions. There is a stronger distinction here: every holomorphic function has harmonic real and imaginary parts, but a general harmonic function need not have a globally defined harmonic conjugate on a domain with holes. The mean-value property is local, while existence of a global conjugate is sensitive to periods. Cauchy's formula lets those local and global stories sit in one framework without conflating them.

Finally, the boundary values determine the interior only when they arise from a function holomorphic on the filled region. You cannot feed arbitrary boundary data into Cauchy's formula and assume the resulting expression reproduces those data on the boundary. For instance, a continuous real-valued function prescribed on a circle may have a harmonic extension, but unless it is compatible with a holomorphic function's boundary trace, the Cauchy integral does not act as a generic interpolation formula. Cauchy's theorem is rigid precisely because its input already satisfies a strong interior condition.

A particularly clean use of the derivative estimate is the polynomial-growth result when the bound is centered somewhere other than zero. Suppose $|f(z)|\le A(1+|z|)^m$ on the entire plane, and fix any $a$. On $|z-a|=R$, the triangle inequality gives $|z|\le |a|+R$, so
$$
|f^{(n)}(a)|\le \frac{n!A(1+|a|+R)^m}{R^n}.
$$
For $n>m$, the right side tends to zero as $R\to\infty$. Thus every derivative above order $m$ vanishes at every point. This is the higher-order version of Liouville's theorem, and it shows exactly how a global growth rate constrains algebraic degree. The use of arbitrarily large circles is essential: a bounded function on just one disk need not be a polynomial or constant.

Cauchy's formula also proves uniqueness from boundary values with little effort. If $f$ and $g$ are holomorphic on a neighborhood of a closed disk and agree at every point of its boundary circle, apply the formula to $f-g$. Every interior value is an integral of zero, so $f=g$ throughout the disk. You do not need to check derivatives or invoke the identity theorem. The result is stronger than a numerical interpolation statement: infinitely many interior values are forced simultaneously. It also explains why a supposed compactly supported holomorphic “bump” cannot exist on a connected region. Outside its support it vanishes on an open set; analytic continuation then forces it to vanish everywhere.

The filled-region hypothesis is easy to test with a counterexample. Set $f(z)=1/z$ and integrate $f(z)/(z-a)$ around $|z|=2$ for a point $a$ with $0<|a|<2$. The integrand has poles at both $a$ and zero. If you apply Cauchy's formula as though $f$ were holomorphic throughout the disk, you predict $2\pi i/a$. But partial fractions give $1/[z(z-a)]=(1/a)[1/(z-a)-1/z]$, and the two contour integrals cancel. The actual result is zero. Cauchy's formula does not fail; its hypothesis on the interior fails. The example is useful because $f$ is perfectly holomorphic near the *contour*, so checking only the boundary would miss the problem.

## 4. Series and singularities

### Taylor series come from a contour, not a smoothness guess

Suppose $f$ is holomorphic on an open disk $|z-a|<R_0$. Choose $0<R<R_0$. Cauchy's formula on the circle $|\zeta-a|=R$ says that for $|z-a|<R$,
$$
f(z)=\frac{1}{2\pi i}\int_{|\zeta-a|=R}\frac{f(\zeta)}{\zeta-z}\,d\zeta.
$$
Now factor the kernel as a geometric series:
$$
\frac1{\zeta-z}
=\frac1{\zeta-a}\frac1{1-(z-a)/(\zeta-a)}
=\sum_{n=0}^{\infty}\frac{(z-a)^n}{(\zeta-a)^{n+1}}.
$$
For $|z-a|\le r<R$, the ratio in the geometric series has modulus at most $r/R<1$ uniformly for every $\zeta$ on the circle. We may therefore integrate term by term and obtain
$$
f(z)=\sum_{n=0}^{\infty}c_n(z-a)^n,
\qquad c_n=\frac{1}{2\pi i}\int_{|\zeta-a|=R}
\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta
=\frac{f^{(n)}(a)}{n!}.
$$
This proves much more than the existence of derivatives. It says that, on every smaller closed disk, the Taylor series converges uniformly to the function. The same geometric majorant controls the differentiated series on a still smaller disk, so termwise differentiation is valid there. The larger circle supplies a bound on the tail: if $M_R=\max_{|\zeta-a|=R}|f(\zeta)|$ and $|z-a|\le r<R$, then Cauchy's coefficient estimate $|c_n|\le M_R/R^n$ gives
$$
\left|f(z)-\sum_{n=0}^{N}c_n(z-a)^n\right|
\le M_R\frac{(r/R)^{N+1}}{1-r/R}.
$$
Uniform convergence is doing real work here. Pointwise convergence alone would not justify taking the limit through the contour integral, nor would it give a uniform error guarantee across the smaller disk.

One useful consequence is *uniqueness of analytic continuation*. If two holomorphic functions agree on a small open disk inside a connected domain, their Taylor coefficients agree there. The identity theorem then propagates equality through overlapping disks across the connected domain. More generally, agreement on a set with an accumulation point inside the domain is enough. This does not mean a Taylor series around one center converges across the whole domain; it means the function, if continued holomorphically along a route, has no freedom to change values arbitrarily. The distinction between uniqueness of continuation and radius of convergence becomes important when singularities lie between one center and another.

The coefficient bound also explains why a holomorphic function cannot have a Taylor series with a mysterious collection of coefficients unrelated to its derivatives. Once the function is fixed on any surrounding circle, Cauchy's integrals fix every $c_n$. For instance, $e^z$ has derivatives $e^z$ of all orders, so about zero
$$
e^z=\sum_{n=0}^{\infty}\frac{z^n}{n!}
$$
with infinite radius of convergence. The series is not just a way of defining the exponential; it can be recovered from any small contour on which the exponential is known. By contrast, $\operatorname{Log}(1+z)$ has derivative $1/(1+z)$ and, on $|z|<1$ with the branch taking value zero at $z=0$,
$$
\operatorname{Log}(1+z)
=z-\frac{z^2}{2}+\frac{z^3}{3}-\cdots.
$$
The obstruction at $z=-1$ limits this Taylor series to radius $1$. Its branch cut controls which continuation is chosen beyond the disk; the singular point itself controls the radius.

The radius of convergence of the Taylor series centered at $a$ reaches at least as far as the largest disk centered at $a$ on which $f$ is holomorphic. It can sometimes extend beyond a particular domain we happened to choose; what matters is the function's analytic continuation and its nearest obstruction. For example,
$$
\frac1{1-z}=\sum_{n=0}^{\infty}z^n,\qquad |z|<1.
$$
The function makes sense at many points with $|z|>1$, but this series cannot reach them: its pole at $z=1$ fixes radius $1$. Recenter at $a=2$ and a new Taylor series works near $2$. A series is a local representation with a specific center, not a global identity on every part of the function's domain.

The phrase “nearest singularity” needs its domain attached. A branch cut chosen for $\operatorname{Log}$ is a boundary of one branch, but many points on the cut are not intrinsic singularities of the multivalued logarithm. You may continue a branch around one side of the origin and choose a new cut. A full circuit around zero changes the value by $2\pi i$, so continuing all the way back does not return to the original branch. This is why continuation along different paths can matter, while the Taylor series in one disk is unambiguous.

### Laurent series separate the two sides of a hole

If $f$ is holomorphic in an annulus $A=\{z:r<|z-a|<R\}$, the appropriate expansion is a *Laurent series*
$$
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-a)^n,
\qquad
c_n=\frac1{2\pi i}\int_{|\zeta-a|=\rho}
\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta,
\quad r<\rho<R.
$$
The coefficients do not depend on which admissible circle $\rho$ we choose: the difference of two such circles bounds an annular region where the integrand is holomorphic. To see where positive and negative powers come from, take an inner circle $\rho_1<|z-a|$ and an outer circle $\rho_2>|z-a|$. The annular Cauchy formula is the outer-circle integral minus the inner-circle integral. Expand the outer kernel in $(z-a)/(\zeta-a)$ to get nonnegative powers. Expand the inner kernel in $(\zeta-a)/(z-a)$ to get negative powers. Both expansions are uniform on any closed subannulus $r+\delta\le|z-a|\le R-\delta$. This compact-subannulus convergence permits termwise contour integration and differentiation.

The negative powers record information hidden in the hole. If all negative coefficients vanish, the Laurent series becomes a Taylor series and extends across the center. If finitely many remain, the center is a pole. If infinitely many remain, it is essential. The positive-power side is the ordinary holomorphic variation that would remain after subtracting the singular behavior. This division makes Laurent series especially useful for local diagnosis: you can ask which term survives a contour integral without calculating the entire function elsewhere.

For example, on $0<|z|<1$,
$$
\frac1{z(1-z)}=\frac1z+\sum_{n=0}^{\infty}z^n.
$$
The same rational function has a different Laurent expansion on $|z|>1$:
$$
\frac1{z(1-z)}
=-\frac1{z^2}\frac1{1-1/z}
=-\sum_{n=2}^{\infty}z^{-n}.
$$
The region of convergence is part of each statement. Writing down a Laurent formula without its annulus can silently change which poles are enclosed and even which coefficient is the residue.

### Three Laurent annuli in one calculation

Take
$$
G(z)=\frac{1}{(z-1)(z-2)}
=-\frac1{z-1}+\frac1{z-2}.
$$
Centered at zero, its singular radii are $1$ and $2$. These radii divide the punctured plane into three maximal circular annuli on which a Laurent expansion about zero can converge. For $|z|<1$, expand both simple fractions in nonnegative powers:
$$
\begin{aligned}
G(z)
&=\frac1{1-z}-\frac1{2-z}\\
&=\sum_{n=0}^\infty z^n-\frac12\sum_{n=0}^\infty\left(\frac z2\right)^n,
\qquad |z|<1.
\end{aligned}
$$
The constant coefficient is $1/2$. No negative powers occur, as expected: the entire disk bounded by any centered circle of radius below one contains no singularity.

In the middle annulus $1<|z|<2$, the first fraction must be expanded in inverse powers while the second remains a positive-power series:
$$
\begin{aligned}
G(z)
&=-\frac1{z}\frac1{1-1/z}
-\frac12\frac1{1-z/2}\\
&=-\sum_{n=0}^\infty z^{-n-1}
-\frac12\sum_{n=0}^\infty\left(\frac z2\right)^n,
\qquad 1<|z|<2.
\end{aligned}
$$
The coefficient of $z^{-1}$ is $-1$, the residue at $z=1$. A centered circle with radius in this annulus encloses that pole and excludes the pole at $2$. Notice that the coefficient of $z^0$ is now $-1/2$, not the value $1/2$ from the inner disk. Laurent coefficients are attached to the annulus and its contour integrals; they are not globally fixed by a formula and a center alone.

For $|z|>2$, expand both fractions in inverse powers:
$$
\begin{aligned}
G(z)
&=-\frac1z\frac1{1-1/z}
+\frac1z\frac1{1-2/z}\\
&=-\sum_{n=0}^\infty z^{-n-1}
+\sum_{n=0}^\infty 2^n z^{-n-1}\\
&=\sum_{n=0}^\infty(2^n-1)z^{-n-1},
\qquad |z|>2.
\end{aligned}
$$
Now the coefficient of $z^{-1}$ is $2^0-1=0$: both poles are enclosed, and their residues $-1$ and $+1$ cancel. The coefficient of $z^{-2}$ is $1$, consistent with the leading behavior $G(z)\sim z^{-2}$ at infinity. This is a useful consistency check: if the $z^{-1}$ term remained, the rational function would decay like $1/z$, contradicting its actual denominator degree.

The region restrictions can be read directly from the geometric series. The expansion of $(1-1/z)^{-1}$ requires $|1/z|<1$, while $(1-z/2)^{-1}$ requires $|z/2|<1$. Their simultaneous validity gives the middle annulus. A formula may be algebraically true after analytic continuation elsewhere, but the displayed series does not converge there. In particular, the two boundary circles are excluded because one of the geometric ratios has modulus one.

There is also a topological reading. As a centered contour expands past radius one, its integral changes from zero to $-2\pi i$. It does not change while the contour moves within $1<|z|<2$. Expanding past radius two adds $2\pi i$ and returns the integral to zero. Since the contour integral of a Laurent series is $2\pi i$ times its $z^{-1}$ coefficient, the three coefficient values $0,-1,0$ encode exactly these changes. The power-series algebra and residue theorem are two descriptions of the same contour behavior.

One can see the same stability directly from the coefficient integral. Fix an integer $k$ and let $\rho_1,\rho_2$ be two radii in the same annulus. The integrand $G(z)z^{-k-1}$ is holomorphic on the closed ring between those circles, so the integral on the outer circle equals the integral on the inner circle with positive circular orientation. Consequently the coefficient $c_k$ is independent of $\rho$ as long as the circle stays within that annulus. If a pole lies between the radii, this deformation hypothesis fails and the two coefficient integrals can differ by its residue. Thus “the Laurent coefficient” is well-defined only after the annular region has been specified.

The annulus boundaries also identify the convergence limit without summing a series. The middle expansion cannot converge on $|z|=1$ or $|z|=2$ as a normally convergent Laurent series on a neighborhood of either boundary: those circles contain singularities of the represented function. For general holomorphic functions, the maximal annulus of convergence is bounded by the nearest singularity on each side, though continuation may still define the function beyond one side through a different expansion. In this rational example the poles sit exactly on the boundary circles, making the two radii transparent.

### Convergence and singularity traps

Convergence regions are easier to understand if you derive each geometric expansion from its inequality. For a Taylor series, the nearest obstruction sets the convergence radius from its center, but the word “obstruction” is more accurate than blindly reading the distance to a marked cut. The function $\operatorname{Log}(1+z)$ near zero has an intrinsic branch point at $-1$, so radius $1$ is unavoidable. A chosen logarithm cut may extend leftward from $-1$, yet its other points are not independent singularities; one can continue around them using another branch. For a rational function, by contrast, an actual pole nearest the center directly limits the series. If a displayed formula has a removable denominator zero, cancel it first; that point does not limit the Taylor expansion of the holomorphic extension.

The coefficients themselves encode boundary control. If $f$ is holomorphic for $|z-a|<R_0$, fix $R<R_0$ and let $M_R$ be its maximum on $|z-a|=R$. Then $|c_n|\le M_R/R^n$. Given $r<R$, the tail after degree $N$ is at most $M_R(r/R)^{N+1}/(1-r/R)$. This is not just a convergence proof; it is a way to decide how many terms are needed at a target point. If $r/R=1/2$, each additional term roughly halves the guaranteed tail. If $r/R=0.99$, the same bound converges slowly. Recenter or choose a larger admissible circle before blaming the series method.

There is a useful reciprocal test for poles. Suppose $f$ is holomorphic on a punctured disk about $a$ and $|f(z)|\to\infty$ as $z\to a$. Then $1/f$ is holomorphic on a sufficiently small punctured disk, tends to zero, and extends holomorphically by setting its value at $a$ to zero. Its zero has some finite positive order $m$, unless $1/f$ is identically zero, which is impossible. Thus $f$ has a pole of order $m$. The stronger condition $|f(z)|\to\infty$ matters. The function $e^{1/z}$ is unbounded near zero, but it also tends to zero along the negative real axis, so this reciprocal argument does not classify it as a pole.

An essential singularity can have residue zero, nonzero, or no useful finite-term shortcut. The function $e^{1/z^2}=1+z^{-2}+(2!)^{-1}z^{-4}+\cdots$ has an essential singularity at zero but no $z^{-1}$ term, so its residue is zero. The function $z^{-3}e^{1/z}$ is also essential, and its residue is the coefficient produced by $z^{-3}\cdot z^2$—but $e^{1/z}$ has no positive powers, so here the residue is zero too. In contrast, $e^{z+1/z}$ has both positive and negative powers; several products can contribute to $z^{-1}$, so one must collect an infinite but convergent coefficient sum or use another method. The singularity type does not determine the residue by itself.

For a more transparent product calculation, use
$$
\frac{e^z}{z^2}=\frac1{z^2}+\frac1z+\frac12+\frac z6+\cdots.
$$
This is a pole of order two with residue $1$, even though the leading singular term is $z^{-2}$. Looking only at the most divergent term would miss the contour integral. Similarly, $\sin z/z^3=z^{-2}-1/6+z^2/120-\cdots$ has a pole of order two and residue zero. These two examples have the same pole order but different residues. A residue is a particular coefficient, not a measure of the singularity's overall severity.

The phrase “isolated singularity” must also be checked before the three-way classification. The function $1/\sin(1/z)$ has poles at $z=1/(n\pi)$ accumulating at zero. There is no punctured disk about zero on which the function is holomorphic: every such disk contains more poles. Therefore zero is not an isolated singularity of this function, and a single Laurent series on $0<|z|<R$ cannot classify it. A drawing may make zero look like a dramatic essential point, but the hypotheses for the classification fail before the series begins.

There is a clean test for a removable singularity that does not start with a Laurent calculation. If $f$ is holomorphic on $0<|z-a|<R$ and has a finite limit $L$ as $z\to a$, define $f(a)=L$. The extension is continuous, but why is it holomorphic at $a$? The boundedness test makes the negative Laurent coefficients vanish, so its local representation is a Taylor series and the extension is holomorphic. Without that theorem, continuity at a newly filled point alone would not automatically prove complex differentiability there. This logical distinction matters when you remove a singularity inside a larger argument and then apply Cauchy's formula across the filled point.

The behavior of $\sin(1/z)$ gives a useful counterpoint. It is holomorphic on every punctured disk about zero and has infinitely many negative Laurent terms, so zero is essential. Its zeros $1/(n\pi)$ accumulate at zero without violating the identity theorem, because the accumulation point is outside the domain. Its reciprocal $1/\sin(1/z)$, however, has poles at exactly those points and is not holomorphic on any full punctured disk. Taking a reciprocal can therefore change the *isolation* question before it changes the singularity type. Always recheck the domain after an algebraic operation.

Convergence at an annulus boundary is a separate question from convergence in its open interior. The Laurent theorem guarantees the expansion on $r<|z-a|<R$ and locally uniform convergence there. It does not decide what happens at $|z-a|=r$ or $R$ point by point. A boundary circle containing a pole is hopeless as a complete contour of convergence, but a series may converge at some other boundary points under additional conditions. Do not use the interior proof to justify termwise contour integration exactly on a limiting boundary without a new bound. Move the contour strictly inside the annulus, perform the calculation, and handle any boundary limit explicitly.

The Taylor series of $1/(1+z^2)$ makes the radius issue concrete without a branch cut. The geometric expansion gives
$$
\frac1{1+z^2}=\sum_{n=0}^{\infty}(-1)^nz^{2n},\qquad |z|<1.
$$
Its nearest singularities are the poles at $i$ and $-i$, both at distance $1$ from the center. On $|z|=1$ the terms have modulus $1$, so they do not even tend to zero and the series diverges at every boundary point. Yet the rational function is perfectly regular at many of those points, including $z=1$. Recenter at $1$ and a different Taylor series describes it there. A failure of one centered series on its boundary is not a failure of the function to exist at that point.

### The principal part tells you what failed

An *isolated singularity* at $a$ means $f$ is holomorphic on some punctured disk $0<|z-a|<R$. Its *principal part* consists of the negative-power terms in the Laurent expansion. Exactly three cases occur.

A singularity is *removable* if every negative coefficient vanishes. Then define $f(a)=c_0$ and obtain a holomorphic extension. For $f(z)=\sin z/z$ at $0$, the sine series gives
$$
\frac{\sin z}{z}=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots,
$$
so $f(0)=1$ removes the apparent defect. A useful equivalent test is local boundedness: a holomorphic function on a punctured disk that stays bounded near its center has a removable singularity. Cauchy's coefficient formula on shrinking circles shows its negative coefficients are zero.

Here is the coefficient argument in one line. If $|f(z)|\le M$ near $a$ and $k\ge1$, integrate on $|z-a|=\rho$ to obtain
$$
|c_{-k}|=\left|\frac1{2\pi i}\int_{|z-a|=\rho}
f(z)(z-a)^{k-1}\,dz\right|\le M\rho^k.
$$
As $\rho\to0$, the coefficient must be zero. This proves the removable-singularity theorem without assuming the limit of $f$ at $a$ in advance. The limit follows after the negative terms vanish. The argument is a good example of Cauchy's machinery turning a simple size bound into a strong structural conclusion.

A *pole of order $m$* has a finite nonzero principal part ending in $c_{-m}(z-a)^{-m}$, where $c_{-m}\ne0$. Equivalently, $(z-a)^m f(z)$ extends holomorphically and is nonzero at $a$. For $f(z)=1/(z-2)^3$, the point $2$ is a pole of order $3$; the function's modulus grows without bound as $z\to2$. Be careful with the converse phrase “unbounded near $a$”: it identifies a pole only if $|f(z)|\to\infty$ as $z\to a$, not merely if $f$ takes arbitrarily large values near $a$.

An *essential singularity* has infinitely many negative Laurent coefficients. For $f(z)=e^{1/z}$ at $0$,
$$
e^{1/z}=1+\frac1z+\frac1{2!z^2}+\cdots.
$$
Along positive real $z\to0$, the modulus blows up; along negative real $z\to0$, it tends to zero; along imaginary approaches it oscillates. No value or finite-order pole can repair this behavior. A deeper result, the Casorati–Weierstrass theorem, says values of a function near an essential singularity are dense in $\mathbb C$. We do not need that theorem for residue calculations, but it explains why essential singularities resist the simple pole picture. The classification assumes *isolation*: a cluster of singularities accumulating at $a$ requires a different analysis.

Do not infer the type of an isolated singularity from one approach path. The function $e^{1/z}$ grows along one ray and shrinks along another, while a pole satisfies $|f(z)|\to\infty$ along *every* approach to its center. Nor does a bounded-looking plot prove removability: finite resolution can miss a narrow growth direction. The Laurent principal part or a theorem with verified hypotheses supplies the classification. Conversely, if a symbolic expression seems complicated but you can prove it bounded on a punctured disk, the removable-singularity theorem settles the issue without a full series expansion.

## 5. Residues and contour methods

### One Laurent coefficient survives a loop

If $f$ has an isolated singularity at $a$ with Laurent series $\sum c_n(z-a)^n$, define its *residue* by $\operatorname{Res}(f,a)=c_{-1}$. Parametrise a small counterclockwise circle and integrate term by term; every integer power except $(z-a)^{-1}$ integrates to zero. Thus
$$
\int_{|z-a|=r}f(z)\,dz=2\pi i\operatorname{Res}(f,a),
$$
provided the circle lies in a Laurent annulus with no other singularities. This is why residues matter: the contour discards the entire local expansion except one coefficient.

At a simple pole, if $f(z)=g(z)/h(z)$ with $g,h$ holomorphic near $a$, $h(a)=0$, and $h'(a)\ne0$, then
$$
\operatorname{Res}(f,a)=\frac{g(a)}{h'(a)}.
$$
For a pole of order $m$, provided $(z-a)^mf(z)$ extends holomorphically near $a$,
$$
\operatorname{Res}(f,a)
=\frac1{(m-1)!}\left.\frac{d^{m-1}}{dz^{m-1}}
\bigl[(z-a)^mf(z)\bigr]\right|_{z=a}.
$$
These are shortcuts to a coefficient, not new definitions. At an essential singularity a Laurent expansion may still make the answer easy: $\operatorname{Res}(e^{1/z},0)=1$. There is no requirement that a residue belong to a pole.

The formulas can be checked against a local expansion rather than trusted as recipes. For $f(z)=e^z/(z-1)^3$, expand $e^z=e\,e^{z-1}=e[1+(z-1)+(z-1)^2/2+\cdots]$. Dividing by $(z-1)^3$ shows that the coefficient of $(z-1)^{-1}$ is $e/2$. The order-three pole formula gives the same answer: differentiate $(z-1)^3f(z)=e^z$ twice and divide by $2!$. Hence a small positive loop around $1$ gives $2\pi i(e/2)=\pi i e$, exactly the derivative-formula result from Section 3. Three perspectives—Taylor expansion, Cauchy's derivative formula, and residue—describe one calculation.

For a rational function, always locate and cancel removable factors before declaring poles. The expression $(z^2-1)/(z-1)$ has a denominator zero at $1$ as written, but it equals $z+1$ away from $1$ and extends holomorphically there; its residue is zero. By contrast, $(z+1)/(z^2-1)$ reduces to $1/(z-1)$ away from $-1$, so $-1$ is removable while $1$ is a simple pole. The distinction changes which points belong in a residue sum. It also affects numerical work: evaluating an uncancelled expression very near a removable point can suffer severe cancellation even though the mathematical function is regular.

Now let $C$ be a positively oriented piecewise smooth simple closed contour. Suppose $f$ is holomorphic on an open neighborhood of $C$ and its interior except at finitely many isolated points $a_1,\ldots,a_N$ strictly inside $C$, and suppose no singularity lies on $C$. Excise disjoint small disks around the $a_j$. Cauchy–Goursat on the punctured region gives the outer integral equal to the sum of counterclockwise inner-circle integrals. Shrink those circles, or use their Laurent expansions, to obtain the *residue theorem*
$$
\int_C f(z)\,dz=2\pi i\sum_{j=1}^{N}\operatorname{Res}(f,a_j).
$$
For a non-simple closed contour whose trace avoids the singularities, the weighted form replaces each residue by $\operatorname{Ind}(C,a_j)\operatorname{Res}(f,a_j)$, under appropriate homology conditions in the holomorphy region. In all examples below, the contours are simple and counterclockwise unless stated otherwise. A clockwise contour reverses the sign. If a pole is on the contour, the ordinary integral and the theorem's hypotheses fail; an indentation or a principal-value prescription is a new problem, not a silent half-residue rule.

The punctured-domain proof makes the bookkeeping tangible. Draw an outer boundary around two poles and small counterclockwise circles $C_1,C_2$ around each one. The oriented boundary of the *punctured* region is the outer path together with $-C_1$ and $-C_2$. Cauchy–Goursat gives
$$
0=\int_C f(z)\,dz-\int_{C_1}f(z)\,dz-\int_{C_2}f(z)\,dz.
$$
Each inner integral is $2\pi i$ times its local residue. That is all the residue theorem adds: a global contour decomposes into local loops. The theorem is powerful because the local coefficient often needs only one derivative or a short partial fraction, while direct parametrisation of the outer curve may be ugly.

As a rational example, let $C:|z|=3$ and $f(z)=z/(z^2+1)$. Both poles $i$ and $-i$ lie strictly inside. The simple-pole formula gives residue $i/(2i)=1/2$ at $i$ and $(-i)/(2(-i))=1/2$ at $-i$. Thus $\int_C f(z)\,dz=2\pi i$. One can cross-check using the expansion at infinity: $z/(z^2+1)=z^{-1}-z^{-3}+\cdots$ for $|z|>1$, so the $z^{-1}$ coefficient is $1$. If the contour instead enclosed only one pole, the answer would be $\pi i$. The formula therefore encodes contour location as well as local algebra.

### Choosing and checking a residue calculation

Residue calculations are fastest when you choose the method that exposes the coefficient with the least algebra. For a simple pole of $g/h$ where $h(a)=0$ and $h'(a)\ne0$, use $g(a)/h'(a)$. For a repeated rational pole, expand the analytic factor or use the derivative formula. For products of an exponential and a rational function, a short Taylor expansion often shows the answer more clearly than repeated quotient differentiation. Before applying any formula, factor the denominator, locate the contour, and cancel removable factors. The residue is local, but the contour integral also needs a global inventory of which singularities are enclosed.

Take
$$
f(z)=\frac{z^2+1}{(z-1)^2(z+2)}.
$$
At $z=-2$ the pole is simple, so
$$
\operatorname{Res}(f,-2)
=\left.\frac{z^2+1}{(z-1)^2}\right|_{z=-2}=\frac59.
$$
At $z=1$ the pole is of order two. Set $g(z)=(z^2+1)/(z+2)$; then the residue is $g'(1)$. Differentiating gives $g'(z)=[2z(z+2)-(z^2+1)]/(z+2)^2$, hence $g'(1)=4/9$. On $|z|=3$ both poles lie inside and the residues sum to $1$, so the contour integral is $2\pi i$. The expansion at infinity checks the arithmetic: $f(z)=z^{-1}+O(z^{-2})$, so a large circle must read off coefficient $1$. This cross-check is cheap and catches a sign error at one pole.

At a multiple zero of the denominator, the simple-pole quotient formula is invalid because $h'(a)=0$. For example, $e^z/(z-1)^2$ has residue $e$, found by expanding $e^z=e[1+(z-1)+\cdots]$ or differentiating $(z-1)^2f(z)=e^z$ once. Substituting $a=1$ into $g/h'$ would divide by zero and says nothing. The issue is the order of vanishing of the denominator after cancellation, not the visual complexity of the original formula.

Sometimes partial fractions are the shortest route because they separate pole contributions. For distinct $a,b$,
$$
\frac1{(z-a)(z-b)}
=\frac1{a-b}\frac1{z-a}+\frac1{b-a}\frac1{z-b}.
$$
The residues are opposites. A contour enclosing both has integral zero, while one enclosing only $a$ has integral $2\pi i/(a-b)$. This also explains why a rational function that decays like $z^{-2}$ at infinity has residue sum zero over all finite poles: a large circle integral tends to zero by the ML bound. More generally, the coefficient of $z^{-1}$ in a Laurent expansion valid outside all finite poles equals the sum of their residues. That coefficient provides a global arithmetic check without introducing the residue at infinity formalism.

The contour can simplify a parameter-dependent integral, but the parameter must be included in the estimate. Suppose $a>0$ and $t>0$, and consider $e^{itz}/(z^2+a^2)$. On the upper semicircle, $|e^{itz}|=e^{-t\Im z}\le1$; the rational factor supplies the $R^{-2}$ decay needed for the arc to vanish. If instead the exponential were $e^{-itz}$, its modulus would be $e^{t\Im z}$ on that same arc and could overwhelm the rational decay. Close below for that sign. “Choose the half-plane containing the convenient pole” reverses the logic: choose a contour whose added paths can be controlled, then sum the poles it encloses.

Poles on the path are a different failure mode. Consider $\int_{-1}^{1}dx/x$. The two one-sided improper integrals do not converge, although the symmetric principal value is zero. An upper indentation around zero from $-\varepsilon$ to $+\varepsilon$ is a clockwise half-circle, parametrised by $z=\varepsilon e^{i\theta}$ with $\theta$ decreasing from $\pi$ to $0$. It contributes
$$
\int_{\mathrm{upper\ indent}}\frac{dz}{z}
=i\int_{\pi}^{0}d\theta=-i\pi.
$$
A lower indentation along the same left-to-right passage contributes $+i\pi$. The differing signs are geometric, not a mysterious convention attached to the pole. Neither indentation turns the original divergent improper integral into a convergent one. State the principal-value or indentation prescription before using a half-residue mnemonic.

Essential singularities can still be approachable by coefficient extraction. For $f(z)=e^{1/z}\sin z$, write $e^{1/z}=\sum_{n\ge0}z^{-n}/n!$ and $\sin z=\sum_{k\ge0}(-1)^kz^{2k+1}/(2k+1)!$. A $z^{-1}$ term occurs when $-n+2k+1=-1$, or $n=2k+2$. Therefore
$$
\operatorname{Res}(e^{1/z}\sin z,0)
=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+2)!(2k+1)!}.
$$
The series converges absolutely. A residue need not have a short elementary form; coefficient extraction remains valid because both series converge normally on every compact annulus around zero. The example also shows why multiplying just the first few terms can give a plausible but incomplete answer when infinitely many pairs contribute to the desired power.

For residues of quotients with a non-simple zero in the denominator, first factor out the known vanishing order. If $h(z)=(z-a)^mq(z)$ with $q(a)\ne0$, then $g(z)/h(z)=(z-a)^{-m}g(z)/q(z)$. The residue is the coefficient of $(z-a)^{m-1}$ in the Taylor series of the *regular* factor $g/q$. This formulation is often easier to use than memorizing the repeated-pole derivative formula. If $g$ also vanishes at $a$, its order may cancel some or all of the pole; determine that cancellation before assigning $m$. For instance, $(z-a)^2e^z/(z-a)^3=e^z/(z-a)$ has a simple pole with residue $e^a$, not a third-order pole.

One can often verify a residue calculation by integrating on two convenient circles. Take $f(z)=z/(z^2+1)$ and radii $1/2$ and $2$. The smaller circle contains no pole, so its integral is zero. The larger contains both poles, whose residues sum to $1$, so its integral is $2\pi i$. The two answers differ because the annulus between the circles contains both $i$ and $-i$. If you had found the same answer on both circles by an unjustified deformation, this comparison would expose the missing poles. For a circle whose radius passes through $1$, the integrand has poles on the path; neither calculation applies until you change the contour.

The residue at a simple pole can also be found as a limit: if $(z-a)f(z)$ extends holomorphically to $a$, then $\operatorname{Res}(f,a)=\lim_{z\to a}(z-a)f(z)$. This test is particularly convenient for trigonometric quotients. At a simple zero $a=k\pi$ of $\sin z$, $\sin'(a)=\cos a=(-1)^k$, so $1/\sin z$ has residue $1/\cos a=(-1)^k$. Around a contour containing several such zeros, list the enclosed integers $k$ and sum their alternating signs. Do not infer from the oscillation that a large-contour integral vanishes: $1/\sin z$ has strong growth near its poles, and a chosen contour may pass arbitrarily close to them. The local residue formula is simple; the global contour estimate is a separate task.

For example, evaluate the positively oriented circle integral
$$
\int_{|z|=2}\frac{e^z}{z^2(z-1)}\,dz.
$$
Both $0$ and $1$ lie inside. The pole at zero has order two, so the higher-order formula gives
$$
\operatorname{Res}\left(\frac{e^z}{z^2(z-1)},0\right)
=\left.\frac{d}{dz}\frac{e^z}{z-1}\right|_{z=0}
=-2.
$$
The pole at one is simple and has residue $e$. Therefore the integral is $2\pi i(e-2)$. A direct partial-fraction expansion near zero would reach the same coefficient: $e^z/(z-1)=-1-2z+O(z^2)$, so division by $z^2$ produces $-z^{-2}-2z^{-1}+O(1)$. This local expansion is a useful sign check on the derivative formula.

Now compare an integral where Cauchy's derivative formula is more direct:
$$
\int_{|z|=3}\frac{\cos z}{(z-i)^4}\,dz.
$$
Since $\cos z$ is entire and $i$ lies inside, Cauchy's formula for the third derivative gives
$$
\frac{2\pi i}{3!}\cos^{(3)}(i)
=\frac{2\pi i}{6}\sin(i)
=\frac{\pi i}{3}\,i\sinh(1)
=-\frac{\pi}{3}\sinh(1).
$$
The sign follows from $\cos'''z=\sin z$ and $\sin(i)=i\sinh(1)$. A residue computation would identify the same coefficient in the Taylor series of $\cos z$ at $i$, but Cauchy's formula states the result immediately. Here there are no other enclosed singularities to list.

For rational functions, a partial fraction decomposition can expose the residue before any derivative. Consider
$$
H(z)=\frac{z^2+1}{z(z-1)(z+1)}.
$$
At zero, the limit shortcut gives residue $(0^2+1)/[(0-1)(0+1)]=-1$. At one it gives $2/[1\cdot2]=1$, and at minus one it gives $2/[(-1)(-2)]=1$. Thus the sum of all finite residues is $1$. This agrees with the coefficient of $1/z$ in the expansion at infinity: $H(z)=1/z+O(1/z^3)$. For a rational function with simple poles, the sum of finite residues equals that coefficient. More generally it is the negative of the residue at infinity, where the latter is defined using the local coordinate $w=1/z$ and the differential $H(z)\,dz$. Naming the convention prevents a common sign confusion about “the residue at infinity.”

### A real integral from a semicircle

Consider $a>0$ and
$$
I=\int_{-\infty}^{\infty}\frac{dx}{x^2+a^2}.
$$
Close the segment $[-R,R]$ with the upper semicircle $|z|=R$, traversed from $R$ to $-R$, so the full contour is counterclockwise. Take $R>a$. The integrand $1/(z^2+a^2)$ has simple poles at $ia$ and $-ia$, only the first inside. Its residue is $1/(2ia)$. On the arc, $|z^2+a^2|\ge R^2-a^2$, so its integral has modulus at most $\pi R/(R^2-a^2)\to0$. Therefore
$$
I=2\pi i\frac1{2ia}=\frac\pi a.
$$
Notice what the contour choice used: the rational integrand decays like $R^{-2}$ while the arc grows like $R$. We did not assume an arc contribution vanishes merely because it is curved or far away.

The choice of upper rather than lower semicircle was arbitrary for this even rational integrand. Closing below would be clockwise and enclose the pole $-ia$, whose residue is $-1/(2ia)$. The product of two sign changes again gives $\pi/a$. That is a useful orientation check. If a calculation using the two half-planes gives opposite answers for a real integral with no real-axis poles, inspect the traversal direction or a derivative in the residue formula. The contour's geometry often reveals the error faster than repeating all the algebra.

For comparison, a rational integrand that behaves like $1/z$ on a large arc cannot generally be dismissed by the crude ML estimate: arc length is order $R$, and the integrand is order $1/R$, leaving an order-one bound. One may need cancellation, a different contour, or a stronger lemma. The denominator degree test is thus a first diagnostic, not a theorem that any rational function works. Likewise, absolute convergence of the real integral should be checked before passing from finite segments to an improper integral; here $1/(x^2+a^2)$ is integrable because it decays like $x^{-2}$.

### A Fourier integral and the sign of the half-plane

Now add an oscillatory factor and let $t>0$:
$$
J(t)=\int_{-\infty}^{\infty}\frac{e^{itx}}{x^2+a^2}\,dx.
$$
In the upper half-plane, $|e^{itz}|=e^{-t\Im z}\le1$, so the same upper semicircle works. The pole at $ia$ contributes residue $e^{-at}/(2ia)$. The same arc bound as above gives $J(t)=\pi e^{-at}/a$. For $t<0$, close in the lower half-plane to retain exponential decay. That contour is clockwise; the pole at $-ia$ has residue $e^{at}/(-2ia)$, and the extra minus sign from orientation gives the same positive result. At $t=0$, the previous rational-integral argument applies. Altogether,
$$
\int_{-\infty}^{\infty}\frac{e^{itx}}{x^2+a^2}\,dx
=\frac\pi a e^{-a|t|},\qquad a>0,\ t\in\mathbb R.
$$
This is a small but useful Fourier-transform pair. It also demonstrates a decision rule: the sign in $e^{itz}$ tells you which half-plane damps the integrand. For functions that grow on arcs, or for contours near a branch cut, the same rule needs a fresh bound; it is not a universal recipe.

You can extract real sine and cosine integrals from the same result. Since $1/(x^2+a^2)$ is even, the sine part is odd and integrates to zero over the symmetric real line. Therefore
$$
\int_0^\infty\frac{\cos(tx)}{x^2+a^2}\,dx
=\frac\pi{2a}e^{-a|t|}.
$$
This half-line formula does not require a new contour: parity gives the factor of two. The step is easy to forget when an application asks for a cosine transform instead of a full Fourier transform. It is also a clean check on the answer: at $t=0$ it reduces to half of the rational integral, and as $|t|$ grows it tends to zero.

For $t>0$, the bound $|e^{itz}|\le1$ on the upper arc was enough because the rational factor already gave $R^{-2}$. For an integrand with only $R^{-1}$ decay, the exponential's stronger angular damping may still make the arc vanish; a result such as Jordan's lemma formalises that estimate under suitable hypotheses. Near the arc's endpoints, however, $\Im z$ is small, so a proof must account for those short regions too. Saying “the exponential decays in the upper half-plane” without handling the endpoints is an incomplete argument.

Laplace transforms use a closely related exponential with a different geometry. For $t\ge0$ and $\Re s>0$, direct integration gives
$$
\int_0^\infty e^{-st}\sin t\,dt
=\Im\!\int_0^\infty e^{-(s-i)t}\,dt
=\frac1{s^2+1}
$$
when $s$ is real and positive; the final rational expression then extends analytically to $\Re s>0$. Inverting a Laplace transform by a Bromwich contour is a separate residue application: for $F(s)=1/(s+a)$ with $a>0$, a vertical line $\Re s=\gamma>-a$ and $t>0$ can be closed to the left under a suitable vanishing-arc estimate, giving $e^{-at}$ from the pole $s=-a$. The line's placement relative to every singularity, growth of $F$ along the closing arc, and the sign of $t$ are essential hypotheses. A formal instruction to “sum the poles” without those checks can give the wrong inverse.

More explicitly, with the common forward-transform convention
$$
F(s)=\int_0^\infty e^{-st}f(t)\,dt,
$$
the inverse integral runs upward along a vertical line $s=\gamma+iy$ placed to the right of every singularity of $F$:
$$
f(t)=\frac1{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty}e^{st}F(s)\,ds,
$$
at positive $t$ under the standard transform and inversion hypotheses. For $F(s)=1/(s+a)$, the product $e^{st}F(s)$ has residue $e^{-at}$ at $-a$. In this simple case direct forward integration verifies the answer: $\int_0^\infty e^{-st}e^{-at}\,dt=1/(s+a)$ when $\Re s>-a$. The contour method becomes more valuable when $F$ has several poles, higher-order poles, or branch structure, but the same caution remains: the inverse integral is defined by a limiting process, and the closing contour must support that limit.

Poles on an intended integration path require a decision that changes the problem. For example, $\int_{-1}^{1}dx/x$ does not exist as an ordinary improper integral: its two one-sided integrals diverge. The Cauchy principal value $\lim_{\varepsilon\to0}\bigl(\int_{-1}^{-\varepsilon}dx/x+\int_{\varepsilon}^{1}dx/x\bigr)$ equals zero by symmetric cancellation, but it is a different object. If a contour passes above or below the pole using a tiny semicircular indentation, the indentation contributes a sign-dependent imaginary term. That contribution is often summarised as a “half residue,” yet the sign and the precise limiting prescription must be stated. The basic residue theorem deliberately excludes poles on the path to keep its statement unambiguous.

### A keyhole contour with two banks

A branch is not decoration added after the algebra. It determines the function being integrated, the contour on which that function is single-valued, and the values on the two banks of a cut. The real integral
$$
I=\int_0^\infty \frac{x^{-1/2}}{1+x}\,dx
$$
is a compact example in which all three choices matter. The integral converges: near zero its integrand is comparable to $x^{-1/2}$, which is integrable, and at infinity it is comparable to $x^{-3/2}$, also integrable. To use residues, extend the power to a slit plane with
$$
z^{-1/2}=\exp\!\left(-\tfrac12\operatorname{Log} z\right),
\qquad 0<\arg z<2\pi.
$$
This is a branch cut along the positive real axis. The upper bank has argument $0$ and value $x^{-1/2}$. The lower bank has argument $2\pi$ and value $e^{-\pi i}x^{-1/2}=-x^{-1/2}$. The sign change is the point of the branch choice; using the principal branch cut on the negative real axis would put the discontinuity somewhere else and require a different contour accounting.

Use a keyhole contour around the positive axis, with outer radius $R$, inner radius $\varepsilon$, and positive orientation around the slit annulus. The upper bank runs from $\varepsilon$ to $R$. The lower bank runs from $R$ back to $\varepsilon$. Since $f(z)=z^{-1/2}/(1+z)$,
$$
\int_{\text{upper bank}} f(z)\,dz
=\int_\varepsilon^R\frac{x^{-1/2}}{1+x}\,dx,
\qquad
\int_{\text{lower bank}} f(z)\,dz
=-\int_R^\varepsilon\frac{x^{-1/2}}{1+x}\,dx
=\int_\varepsilon^R\frac{x^{-1/2}}{1+x}\,dx.
$$
The two banks therefore contribute twice the truncated real integral, not zero. The only pole in the slit annulus is $z=-1$, where this chosen branch has $\arg(-1)=\pi$ and hence $(-1)^{-1/2}=e^{-i\pi/2}=-i$. Its residue is
$$
\operatorname{Res}\left(\frac{z^{-1/2}}{1+z},-1\right)=-i.
$$
The residue theorem gives a total contour integral of $2\pi i(-i)=2\pi$. To identify the real integral with that limit, the circular pieces must vanish. On the outer circle, for $R>1$,
$$
\left|\int_{|z|=R}\frac{z^{-1/2}}{1+z}\,dz\right|
\le 2\pi R\frac{R^{-1/2}}{R-1}
=\frac{2\pi R^{1/2}}{R-1}\longrightarrow0.
$$
On the inner circle, for $0<\varepsilon<1$,
$$
\left|\int_{|z|=\varepsilon}\frac{z^{-1/2}}{1+z}\,dz\right|
\le 2\pi\varepsilon\frac{\varepsilon^{-1/2}}{1-\varepsilon}
=\frac{2\pi\varepsilon^{1/2}}{1-\varepsilon}\longrightarrow0.
$$
The ML estimate uses the maximum of the modulus on each arc and its length $2\pi r$. It matters that the denominator is bounded below by $R-1$ or $1-\varepsilon$; replacing these bounds by an unqualified statement that the arcs are “small” would not prove anything. Taking limits now yields $2I=2\pi$, so $I=\pi$.

This derivation offers three practical checks. First, write the branch and argument interval before evaluating either bank. Second, orient both banks from the contour, not from memory: one travels outward and the other inward. Third, estimate the small and large arcs separately, because their dominant powers differ. As a quick independent check, $x=t^2$ transforms the original integral into $2\int_0^\infty(1+t^2)^{-1}dt=\pi$. That substitution verifies the value, while the keyhole calculation explains how the branch jump creates it.

For a general exponent $0<\alpha<1$, the same contour with $z^{\alpha-1}$ and the cut on the positive axis has bank values in ratio $e^{2\pi i(\alpha-1)}=e^{2\pi i\alpha}$. The origin arc is of order $\varepsilon^\alpha$, and the outer arc is of order $R^{\alpha-1}$. Both vanish precisely in this range. The pole at $-1$ contributes a phase determined by the selected branch. This is a template, not a license to substitute arbitrary complex exponents: convergence, branch values, and arc estimates must all be revisited when the exponent changes.

It is useful to separate a branch cut from the obstruction that makes a global branch impossible. For $z^{-1/2}$, the positive axis is a convenient seam chosen to suit this contour. We could rotate the seam and repeat the calculation, but we could not remove the seam from every loop around zero. Continuing the square root once around zero changes its sign; continuing twice returns the original value. A branch on a simply connected slit domain resolves this ambiguity by specifying which continuation is used. In a contour proof, the two banks are therefore not duplicate copies of one continuous boundary value: they are limits of the chosen branch from different sides.

This distinction helps diagnose branch errors in symbolic work. Suppose an algebraic simplification replaces $\sqrt{z^2}$ by $z$. That identity is valid only on a domain and branch where the selected square root has that value. With principal square roots, it fails for some arguments even though squaring both sides gives the same expression. In the keyhole calculation, replacing $(-1)^{-1/2}$ by $+i$ or $+1$ is not a harmless simplification; it changes the residue theorem's answer. State the branch before evaluating special points, and carry its argument interval through every substitution.

### An arc estimate with a double pole

When a contour is closed to turn a real integral into a residue sum, the residue theorem handles only the closed contour. It does not say that the added arc disappears. Consider
$$
J(a)=\int_{-\infty}^{\infty}\frac{e^{iax}}{(x-i)^2}\,dx,
\qquad a>0.
$$
The real integral is absolutely convergent because its integrand has modulus $1/(x^2+1)$. Close the segment $[-R,R]$ by the upper semicircle $C_R$, counterclockwise. The integrand $F(z)=e^{iaz}/(z-i)^2$ has one pole inside, a double pole at $i$. Its residue is found by differentiating the numerator:
$$
\operatorname{Res}(F,i)
=\left.\frac{d}{dz}e^{iaz}\right|_{z=i}
=ia e^{-a}.
$$
The theorem predicts $2\pi i(ia e^{-a})=-2\pi a e^{-a}$. Now verify the arc. On $z=Re^{i\theta}$, $0\le\theta\le\pi$, we have
$$
|e^{iaz}|=e^{-aR\sin\theta}\le1,
\qquad |z-i|\ge R-1.
$$
The crude ML bound gives
$$
\left|\int_{C_R}F(z)\,dz\right|
\le \frac{\pi R}{(R-1)^2}\longrightarrow0.
$$
This estimate is sufficient even though it ignores the exponential decay away from the endpoints of the arc. The real segment integrals converge to $J(a)$ by absolute convergence, so $J(a)=-2\pi a e^{-a}$. At first glance the negative answer may look odd because the integrand is complex. For $a>0$, the cosine part is even and the sine part is odd; the imaginary contribution cancels on symmetric intervals, while the cosine transform may be negative.

The condition $a>0$ is not cosmetic. If $a<0$, then $|e^{iaz}|=e^{|a|R\sin\theta}$ grows in the upper half-plane, and the estimate above fails. Close in the lower half-plane instead, with clockwise orientation. The pole at $i$ is then outside, so the integral is zero. This is consistent with the contour calculation: the Fourier transform here is one-sided, not even, because $(x-i)^{-2}$ is complex-valued. At $a=0$, the arc estimate still works and the residue at the double pole is zero, giving $\int_{\mathbb R}(x-i)^{-2}dx=0$.

This example separates two decisions that are often collapsed. The sign of the oscillatory parameter selects a half-plane where the exponential does not grow; the pole locations then determine which residues lie inside. A denominator estimate alone can be enough when its algebraic decay beats the arc length, as it does here. For a denominator with only one power, the same crude bound would be order one and would not prove decay. One would need the sharper oscillatory estimate (Jordan's lemma) or another contour. Failure of a bound is not evidence that the arc fails to vanish; it means only that this particular estimate has not settled the question.

### A numerical contour check

One can verify the Cauchy-formula example numerically without confusing the check with its proof. Parametrise $C:|z-1|=r$ by $z(\theta)=1+re^{i\theta}$, take $r=0.4$, and apply the periodic trapezoidal rule:

```python
import cmath
import math

radius = 0.4
for n in (8, 16, 32, 64):
    total = 0j
    for k in range(n):
        theta = 2 * math.pi * k / n
        z = 1 + radius * cmath.exp(1j * theta)
        dz_dtheta = 1j * radius * cmath.exp(1j * theta)
        total += cmath.exp(z) / (z - 1) * dz_dtheta
    estimate = total * (2 * math.pi / n)
    exact = 2j * math.pi * math.e
    print(n, estimate, abs(estimate - exact))
```

The denominator never vanishes on this circle, and increasing $n$ should drive the error down toward floating-point limits. A stable sequence of approximations is evidence that the parametrisation and orientation were coded correctly. It is not a proof of the residue theorem: a grid could miss a narrow feature, a pole could sit almost on the path, or cancellation could make a wrong contour appear plausible.

The numerical experiment is especially clean here because the parametrised integrand simplifies algebraically: $dz/d\theta=i(z-1)$, so $[e^z/(z-1)](dz/d\theta)=ie^z$. This cancellation shows the sampled function is smooth and periodic in $\theta$, which helps the trapezoidal rule. It also gives an independent way to debug the code if an estimate has the wrong sign: $dz/d\theta$ should contain $+i$ for counterclockwise travel. A clockwise parametrisation would contain $-i$ and return $-2\pi i e$. Numerical contour integration is most trustworthy when you inspect the parametrised integrand and the minimum distance from the path to each singularity, not just the final printed number.

## 6. Global theorems and geometric structure

### Local factorisation turns zeros into integers

Let $f$ be holomorphic on a connected domain $D$ and not identically zero. Its zeros are isolated. Indeed, at a zero $a$, Taylor's theorem gives a first nonzero coefficient unless every coefficient vanishes. If every coefficient vanishes, $f$ vanishes on a disk; by propagating overlapping Taylor disks through the connected domain, the *identity theorem* then makes $f$ identically zero, contrary to assumption. Thus for a unique positive integer $m$,
$$
f(z)=(z-a)^m g(z),\qquad g(a)\ne0,
$$
with $g$ holomorphic near $a$. We call $m$ the *multiplicity* of the zero. For $f(z)=z^2(z-1)^3$, zero has multiplicity $2$ and one has multiplicity $3$. A pole of order $p$ has the analogous factorisation $f(z)=(z-a)^{-p}g(z)$ with $g(a)\ne0$. Taking logarithmic derivatives near these points yields
$$
\frac{f'(z)}{f(z)}=
\begin{cases}
\displaystyle \frac{m}{z-a}+\frac{g'(z)}{g(z)}, & \text{zero of order }m,\\[6pt]
\displaystyle -\frac{p}{z-a}+\frac{g'(z)}{g(z)}, & \text{pole of order }p.
\end{cases}
$$
The second term is holomorphic nearby, so a zero contributes residue $+m$ to $f'/f$ and a pole contributes $-p$. This local calculation explains the global counting theorem.

The factorisation also gives a precise local picture of the map near a zero. If $g(a)\ne0$, then for $z$ close to $a$, $g(z)$ changes slowly compared with $(z-a)^m$. A small circle $z=a+re^{it}$ therefore has image approximately $g(a)r^m e^{imt}$: it wraps $m$ times around zero. The approximation can be made exact at the level of winding number because $g$ has no zero on a sufficiently small disk and contributes zero net winding on its boundary. Thus multiplicity is geometric, not merely an algebraic count in a Taylor series. This also explains why numerical root finders can struggle near multiple zeros: locally the inverse map behaves like an $m$th root and is more sensitive to small changes.

The identity theorem behind isolation of zeros has a useful limitation. Its accumulation point must lie *inside* the connected holomorphy domain. The function $\sin(1/z)$ on the punctured plane has zeros $z=1/(n\pi)$ accumulating at $0$, but $0$ is excluded and is an essential singularity. There is no contradiction. Similarly, infinitely many zeros may accumulate at the boundary of a disk without forcing a holomorphic function to vanish identically inside. When you use a zero-counting theorem, check where all the accumulation and boundary points lie.

### Argument principle and Rouché's theorem

Let $C$ be a positively oriented piecewise smooth simple closed contour. Suppose $f$ is meromorphic on an open neighborhood of $C$ and its interior, has only finitely many zeros and poles inside, and has neither zeros nor poles on $C$. Applying the residue theorem to $f'/f$ gives the *argument principle*
$$
\frac1{2\pi i}\int_C\frac{f'(z)}{f(z)}\,dz
=N_Z-N_P
=\operatorname{Ind}(f\circ C,0),
$$
where $N_Z$ and $N_P$ count interior zeros and poles with multiplicity and order. The last expression is the winding number of the image curve $f(C)$ around zero. It explains the domain-coloring picture from Section 1: if $f(z)=z^2$ and $C$ encircles the origin once, the image encircles zero twice. It also explains why a pole winds in the opposite direction.

Consider the meromorphic function $f(z)=(z-1)^2/[z(z-2)]$ on $C:|z|=3/2$, traversed counterclockwise. Inside the circle, $f$ has a double zero at $1$ and a simple pole at $0$; its pole at $2$ lies outside. No zero or pole touches the circle. The argument principle gives
$$
\frac1{2\pi i}\int_{|z|=3/2}\frac{f'(z)}{f(z)}\,dz=2-1=1.
$$
The image of the circle winds once around the origin, even though $f$ has two zeros inside. A phase plot that seems to show “one turn” is therefore not inconsistent with a double zero; the enclosed pole subtracts one turn. This example is why the argument principle counts zeros *minus* poles, and why one should list both before interpreting a winding plot.

For a polynomial, there are no finite poles, so the principle counts all its roots inside a contour. For a rational function, cancellations can make a suspected zero and pole removable; reduce or factor locally first. For a numerical implementation, sampled values of $f(C)$ may suggest a winding number, but the count is only reliable if the continuous image does not pass through zero between samples. The theorem supplies an exact answer when the boundary condition can be proved.

*Rouché's theorem* packages this winding idea into an efficient comparison. Suppose $f$ and $g$ are holomorphic on an open neighborhood of the closure of a bounded region with positively oriented piecewise smooth simple boundary $C$, and assume
$$
|g(z)|<|f(z)|\quad\text{for every }z\in C.
$$
Then $f$ and $f+g$ have the same number of zeros inside $C$, counted with multiplicity. The inequality is *strict* on the entire boundary. It ensures that the homotopy $f_s=f+sg$, $0\le s\le1$, never vanishes on $C$, since $|f_s|\ge|f|-s|g|>0$. The image curves $f_s(C)$ therefore keep the same winding number about zero, and the argument principle gives the zero count. No claim is made that the zeros remain in the same locations.

For a worked count, take $P(z)=z^5+4z+1$ on $|z|=1$. Set $f(z)=4z$ and $g(z)=z^5+1$. On the circle, $|f|=4$ while $|g|\le2<4$. Both functions are entire, so all hypotheses hold; $P$ has exactly one zero in $|z|<1$, counted with multiplicity. The proof does not locate that zero or assert the other four are in any specific sector. It does tell us $P$ has no zero on $|z|=1$, because the strict inequality prevents cancellation there. If we tried to replace $4z$ by $2z$, the simple estimate would give only $|g|\le2$, which is not strict; the theorem would say nothing from that comparison even if the desired root count happened to be true.

Rouché comparisons are often found by looking for a term that dominates on a chosen circle. The circle is a design variable, not an afterthought. For $Q(z)=z^4+3z+1$, the term $3z$ dominates the other two on $|z|=1$, since $|z^4+1|\le2<3$, so $Q$ has one zero in the unit disk. On $|z|=2$, however, $z^4$ has modulus $16$ and $|3z+1|\le7$, so all four zeros lie in $|z|<2$. Combining the two counts shows exactly three zeros lie in $1<|z|<2$, counted with multiplicity. Neither application tells us individual roots, but together they constrain where every root can be. This annular conclusion is a common way to use the theorem in practice.

The strict inequality need hold only on the selected boundary, not throughout its interior. The functions can have complicated behavior inside; that is the point of the theorem. If $g$ is larger than $f$ on the boundary, swap their roles if a useful inequality results. If no term dominates on a circle, try a different radius or a noncircular contour rather than forcing an invalid comparison. The homotopy proof tells you exactly what a valid comparison needs: a continuous path of boundary images that never crosses zero.

### Zero counts and strict boundary margins

The argument principle is especially useful when a function has a known meromorphic form but its zeros are difficult to solve for. Consider $F(z)=z^3/(z-1)^2$ on $|z|=2$, counterclockwise. Zero has multiplicity three, and $1$ is a pole of order two; neither lies on the boundary. Thus $F(C)$ winds once about zero. You can see the same number without drawing $F(C)$: logarithmic differentiation gives
$$
\frac{F'(z)}{F(z)}=\frac3z-\frac2{z-1},
$$
whose residues inside the circle sum to $3-2=1$. A parameterized plot of the image might cross itself and make a visual turn count awkward. The logarithmic derivative turns the problem into local integer arithmetic. It also warns you that if $F$ has a zero on $C$, $F'/F$ has a pole on the path and the integral is not covered by the theorem.

For a less factorized example, let $P(z)=z^4+2z^2+4$. On $|z|=1$, compare the constant $4$ with the remaining terms: $|z^4+2z^2|\le3<4$. Rouché gives zero roots in the unit disk. On $|z|=2$, the leading term has modulus $16$, while $|2z^2+4|\le12<16$, so all four roots lie in $|z|<2$. Consequently all four roots lie in $1<|z|<2$, counted with multiplicity. This is a genuine location result even though no root has been computed. The strict inequalities also prove that neither boundary circle contains a root.

Choosing the comparison term is often a matter of choosing the radius. For $P(z)=z^5+5z^2+1$, on $|z|=1$ the $5z^2$ term dominates because $|z^5+1|\le2<5$. There are exactly two zeros in $|z|<1$. On $|z|=2$, the leading term has modulus $32$, while $|5z^2+1|\le21$, so there are five zeros in $|z|<2$. Hence three lie in the annulus $1<|z|<2$. Trying to use $z^5$ on the unit circle fails because its modulus is only $1$, while the other terms can have size $6$. The theorem is flexible about which piece you call the base function; the inequality decides the valid choice.

An analytic perturbation can be counted without solving a transcendental equation. How many zeros does $e^z-1-2z$ have in a sufficiently small disk about zero? Its Taylor series begins $-z+z^2/2+\cdots$, so zero is simple. To give an explicit radius, use $|z|=1/2$ and compare $-z$ with $g(z)=e^z-1-z$. The exponential series gives
$$
|g(z)|\le\sum_{n=2}^{\infty}\frac{|z|^n}{n!}
\le e^{1/2}-1-\frac12<\frac12=|z|.
$$
Both functions are entire, so Rouché says $e^z-1-2z$ has exactly one zero in $|z|<1/2$, counted with multiplicity. Since $z=0$ is visibly a zero, it is the only one there and is simple. This is stronger than observing a few Newton iterations converge to zero: the boundary inequality excludes hidden roots throughout the disk.

The same reasoning handles zeros of $f(z)-w$ when $w$ varies. Suppose $f$ is holomorphic near a closed disk around $a$, $f(a)=w_0$, and $f(z)-w_0$ has a zero of multiplicity $m$ at $a$ with no other zeros in the disk. On its boundary $C$, continuity gives $\delta=\min_C|f(z)-w_0|>0$. For every $w$ with $|w-w_0|<\delta$, Rouché compares $f(z)-w_0$ with the constant perturbation $w_0-w$. Thus $f(z)-w$ has exactly $m$ zeros inside, counted with multiplicity. This is the local multiplicity picture behind the open mapping theorem: every sufficiently near target value occurs, even at a critical point. The theorem counts solutions but does not promise $m$ distinct solutions; they can merge at a critical value.

The argument principle can also count poles of a rational function without factoring every numerator. Suppose $R(z)=P(z)/Q(z)$ has no zero or pole on $C$, and $P,Q$ have no common factor after cancellation. Then
$$
\frac{R'(z)}{R(z)}=\frac{P'(z)}{P(z)}-\frac{Q'(z)}{Q(z)}.
$$
The integral counts roots of $P$ inside minus roots of $Q$ inside, with multiplicities. For $R(z)=(z^3+1)/(z^2+4)$ on $|z|=3/2$, all three cube roots of $-1$ have modulus $1$ and lie inside, while the poles at $\pm2i$ lie outside. Therefore the image curve $R(C)$ winds three times around zero. One need not parameterize that image, which could be visually convoluted. If $P$ and $Q$ share a factor, cancel it first; otherwise a removable point may be miscounted as both a zero and a pole, even though the net difference happens to cancel.

There is a tempting invalid use of Rouché: estimate $|g(z)|\le|f(z)|$ on $C$ and conclude equal zero counts. Equality is not enough because $f+g$ could vanish on the boundary. On $|z|=1$, let $f(z)=z$ and $g(z)=-1$. Then $|g|=|f|=1$, but $f$ has one zero inside while $f+g=z-1$ has its zero *on* the boundary. The strict sign in the theorem is doing the work of keeping the homotopy away from zero. If a crude bound gives equality, seek a sharper bound or move the contour; do not round a non-strict estimate into a strict one.

Consider
$$
P(z)=z^6+3z^2+z+10.
$$
We want to count roots in the disk $|z|<2$. On its boundary, the constant term has modulus $10$, while the sum of all other terms satisfies
$$
|z^6+3z^2+z|
\le |z|^6+3|z|^2+|z|
=64+12+2=78,
$$
so this decomposition is useless: it does not make the constant dominate. But the leading term does dominate when $|z|=2$, because
$$
|3z^2+z+10|\le 12+2+10=24<64=|z^6|.
$$
Rouché's theorem applied to $f(z)=z^6$ and $g(z)=3z^2+z+10$ says that $P$ has six zeros in $|z|<2$, counted with multiplicity. Since $P$ has degree six, this places every root in that disk. The strict inequality also proves there is no root on its boundary.

To learn more than the total degree, use the smaller circle $|z|=1$. There,
$$
|z^6+z|\le2<7\le|3z^2+10|,
$$
because the reverse triangle inequality gives $|3z^2+10|\ge10-3=7>2$. Thus compare $f(z)=3z^2+10$ with $g(z)=z^6+z$. The function $f$ has no zeros in the unit disk: its roots satisfy $z^2=-10/3$ and have modulus $\sqrt{10/3}>1$. Rouché then says $P=f+g$ has zero roots in $|z|<1$. Combined with the six-root count in radius two, all six roots lie in the annulus $1<|z|<2$.

One should not write $|3z^2+10|\ge 10-3$ without naming the reverse triangle inequality, and one should not compare with $3z^2$ alone because the constant term is larger there. A good Rouché split often groups terms: the function that is easy to count need not be a single monomial. Here $3z^2+10$ has no zeros in the unit disk, which is enough even though it is not a monomial.

The count does not imply that the six roots are simple, evenly spaced, or numerically close to the unit circle. It only gives a multiplicity count in regions whose boundaries have been checked. A root-finding computation can now be used to approximate locations; the theorem supplies a separate global check that no root was missed outside the annulus. If a numerical root appears close to either circle, refine it and evaluate boundary margins carefully, because the proof depends on strict inequalities.

### Maximum modulus and what it forbids

A nonconstant holomorphic function on a connected domain cannot attain a local maximum of its modulus at an interior point. One proof begins with Cauchy's mean-value formula on a small circle centered at $a$:
$$
f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+re^{i\theta})\,d\theta.
$$
If $|f(a)|$ is a local maximum, the triangle inequality forces every value on a sufficiently small circle to have the same modulus and phase as $f(a)$; otherwise the average would have smaller modulus. Thus $f$ is constant on that circle and, by Cauchy's formula, inside it. The identity theorem makes it constant throughout the connected domain. If $f(a)=0$ and $|f|$ has a local maximum there, $f$ is immediately zero nearby. This is the *maximum modulus principle*.

The equality step in the mean-value proof is rigid. The average of points inside a closed disk of radius $M$ can have modulus $M$ only if all points with positive averaging weight lie at the same boundary point of that disk. Different phases would shorten their vector average. If an arc had smaller modulus, continuity would make that loss persist over an interval and again shorten the average. Hence an interior maximum forces $f(a+re^{i\theta})=f(a)$ around each sufficiently small circle. Cauchy's formula carries this constancy into the disk. This geometric argument exposes the mechanism of the theorem without borrowing a real maximum principle.

On a bounded domain $D$ whose closure lies in an open set where $f$ is holomorphic, continuity gives a maximum of $|f|$ on the compact closure. Unless $f$ is constant, the maximum occurs on the boundary. There is also a minimum-modulus statement, but it needs an extra hypothesis: if $f$ has no zeros in $D$, apply maximum modulus to $1/f$ to see that a nonconstant $|f|$ cannot have an interior minimum. If $f$ has a zero inside, its modulus plainly reaches the minimum value zero there. This distinction prevents a common overstatement of the principle.

For example, $f(z)=z$ on the unit disk has $|f(0)|=0$, an interior minimum, because the function vanishes there; it has no interior maximum. The function $f(z)=e^z$ has no zeros, so neither $|f|$ nor $|1/f|$ can attain an interior maximum on any disk unless constant. On the closed unit disk, the largest value of $|e^z|=e^{\Re z}$ occurs at the boundary point $z=1$, and the smallest at $z=-1$. The formula for $|e^z|$ makes this example transparent, but the principle works even when no elementary modulus formula is available.

The *open mapping theorem* is a related consequence: a nonconstant holomorphic function maps open sets to open sets. Near a regular point it follows from the complex inverse function theorem. Near a critical point, local factorisation of $f(z)-f(a)$ shows a small punctured neighborhood of $f(a)$ is still covered, with multiple preimages counted by the zero's multiplicity. This result explains why a nonconstant holomorphic image cannot end abruptly at an interior point. The maximum modulus principle is consistent with it: if $f(D)$ were trapped in a closed disk and touched its boundary at an interior image point, the image could not be open around that point.

The maximum principle connects geometry and analysis. A holomorphic map cannot create a new peak of $|f|$ in the interior. Cauchy's estimates make that boundary control quantitative, and Liouville's theorem follows when the same bound holds on arbitrarily large circles. In potential theory, the real and imaginary parts of $f$ satisfy related maximum principles for harmonic functions; that is why conformal methods can turn boundary data into interior fields.

### Boundary bounds and the order of a zero

The maximum modulus principle can produce quantitative bounds when the boundary values are simpler than the interior formula. Let $f$ be holomorphic on an open neighborhood of the closed disk $|z|\le1$ and suppose $|f(z)|\le3$ on $|z|=1$. Then $|f(z)|\le3$ throughout the disk. If $|f(0)|=3$, the interior point already attains the maximum, so $f$ must be constant with modulus $3$ on the whole disk. If $|f(0)|<3$, the principle allows many functions; it does not say every interior value is substantially below $3$ by one universal gap independent of the function.

For a nontrivial worked bound, suppose $f$ is holomorphic near $|z|\le1$, $f(0)=0$, and $|f(z)|\le1$ on $|z|=1$. The maximum principle first gives $|f|\le1$ in the disk. Define $g(z)=f(z)/z$ for $z\ne0$ and set $g(0)=f'(0)$; the singularity at zero is removable because $f(0)=0$. On the unit circle $|g(z)|=|f(z)|\le1$, so maximum modulus applied to $g$ gives $|g(z)|\le1$ inside. Therefore
$$
|f(z)|\le|z|\qquad(|z|<1).
$$
This is the basic Schwarz lemma bound under a convenient boundary regularity assumption. If equality holds at any nonzero interior point, then $|g|$ attains an interior maximum and $g$ is a constant of modulus one, so $f(z)=e^{i\theta}z$. The equality case matters: a function cannot touch the bound at an interior point and then behave differently elsewhere.

You can use the same division trick when $f$ has a zero of order $m$ at the origin. If $|f|\le1$ on the unit circle and $f(z)=z^mg(z)$ with $g$ holomorphic on the disk, then $|g|\le1$ on the boundary and hence inside. Consequently $|f(z)|\le|z|^m$. A higher multiplicity forces a stronger decay toward the center. This connects a local integer, the order of a zero, to a global boundary bound. If $f$ has other zeros, no part of the argument breaks; only the factor at the origin was needed.

The maximum principle does not assert that $|f|$ is smallest on the boundary. The function $f(z)=z$ has a zero at the center, giving an interior minimum of zero. If $f$ has no zeros, $1/f$ is holomorphic and the same principle applied to $1/f$ prevents a nonconstant interior minimum of $|f|$. The nonvanishing hypothesis is essential. For instance, $f(z)=z^2-1/4$ on the unit disk has two interior zeros, so any claim that its minimum modulus must be on $|z|=1$ is plainly false.

The maximum principle also has a useful half-plane variant. If $u=\Re f$ and $f$ is holomorphic, then $|e^f|=e^u$. If $u$ has a local maximum at an interior point, $|e^f|$ does too. The maximum modulus principle makes $e^f$ constant, and differentiating gives $e^ff'=0$, hence $f$ is constant on the connected domain. Thus a nonconstant harmonic real part of a holomorphic function cannot have an interior local maximum. On a simply connected domain every harmonic function has a conjugate, so the same conclusion holds for harmonic functions there. The harmonic maximum principle is in fact local and holds on general domains, but this route shows how it grows from complex analysis where a conjugate is available.

Finally, be careful when the region is unbounded. A holomorphic function on the upper half-plane can be bounded on its real boundary and unbounded inside: $f(z)=e^{-iz}$ has $|f(x)|=1$ for real $x$, while $|f(iy)|=e^y\to\infty$. The compact-closure argument used on a bounded disk cannot be applied directly to an unbounded half-plane; there is an additional boundary at infinity. To infer an interior bound, one needs a growth condition or a separate argument controlling large arcs. This is the same missing estimate that appears in contour integration. In both settings, a familiar finite-boundary theorem says nothing about an unexamined limit at infinity.

### Conformal maps and their limits

At a point $a$ with $f'(a)\ne0$, the first-order approximation is $f(a+h)=f(a)+f'(a)h+o(|h|)$. Multiplication by $f'(a)$ rotates and scales, so a holomorphic map preserves angles between smooth curves through $a$, including orientation. This is *local conformality*. It says nothing by itself about global one-to-one behavior. The exponential has nonzero derivative everywhere but repeats values every $2\pi i$; $z^2$ is locally conformal away from zero but identifies $z$ and $-z$ on many domains. At zero, $z^2$ has derivative zero, so even local angle preservation in the ordinary sense fails there.

To compute the angle transformation, imagine two smooth curves through $a$ with nonzero tangent vectors $v_1$ and $v_2$. Their image tangents are $f'(a)v_1$ and $f'(a)v_2$. The quotient of image tangents is
$$
\frac{f'(a)v_2}{f'(a)v_1}=\frac{v_2}{v_1},
$$
so the directed angle between them is unchanged. Lengths are locally scaled by $|f'(a)|$. This is an infinitesimal statement; finite triangles need not retain their lengths or straight sides. A conformal map may bend an entire coordinate grid while preserving the angles where its curves cross. If $f'(a)=0$, the tangent calculation divides by zero and higher-order terms determine a different local pattern. For $z^2$ at $0$, angles of rays are doubled rather than preserved.

The simplest global building blocks are Möbius transformations
$$
M(z)=\frac{az+b}{cz+d},\qquad ad-bc\ne0.
$$
On the Riemann sphere $\widehat{\mathbb C}=\mathbb C\cup\{\infty\}$, each is a bijection with a Möbius inverse. In the finite plane it has a pole at $z=-d/c$ when $c\ne0$, and its derivative is $(ad-bc)/(cz+d)^2$ wherever defined. Möbius maps send generalized circles—ordinary circles and straight lines, with a line regarded as a circle through $\infty$—to generalized circles. Translation, rotation/scaling, and inversion $z\mapsto1/z$ generate their basic geometry.

The sphere language accounts cleanly for poles and infinity. When $c\ne0$, $M(-d/c)=\infty$ and $M(\infty)=a/c$; if $c=0$, the map is affine and fixes infinity. A Euclidean line becomes a circle through $M(\infty)$ unless that image is infinity. This observation often predicts a boundary image before any algebra. The real axis is a generalized circle, for example, and $M(z)=(z-i)/(z+i)$ sends it to the unit circle. Which side maps to the disk is decided by testing one point, such as $z=i$.

An explicit canonical map is
$$
M(z)=\frac{z-i}{z+i}.
$$
For $\Im z>0$, $|z-i|<|z+i|$, so $M$ maps the upper half-plane into the unit disk. Points on the real axis satisfy equality and map to its boundary; solving $w=(z-i)/(z+i)$ for $z$ shows the map is bijective between the two open domains. It sends $i$ to $0$. This matters in boundary-value problems: a geometry with a straight boundary can be transferred to a disk where radial symmetries and known kernels are easier to use.

The inverse is explicit:
$$
z=i\frac{1+w}{1-w},\qquad |w|<1.
$$
Its denominator never vanishes in the open disk, and direct substitution shows its imaginary part is positive there. Thus the “into” statement is truly “onto.” The boundary point $w=1$ corresponds to infinity in the upper half-plane, which is why the boundary correspondence makes the most sense on the Riemann sphere. Neither the forward nor inverse map claims a finite continuous value at every point of the extended boundary in ordinary Euclidean coordinates.

Another canonical map is $z\mapsto z^2$ on the open first quadrant. The argument lies in $(0,\pi/2)$, so doubling it lands in $(0,\pi)$: the image is the upper half-plane. This restriction makes squaring injective. Compose it with $M$ to map the quadrant conformally onto the disk. The same formula $z^2$ on all of $\mathbb C$ would not be globally one-to-one, which is why a mapping statement must name its domain as well as its formula.

An advanced existence theorem says these examples are part of a broad pattern. The *Riemann mapping theorem* states that every nonempty simply connected proper open subset $D\subsetneq\mathbb C$ is conformally equivalent to the unit disk: there is a bijective holomorphic map $\phi:D\to\mathbb D$ whose inverse is holomorphic. After choosing a base point $a\in D$, the conditions $\phi(a)=0$ and $\phi'(a)>0$ make the map unique. The theorem does not include $D=\mathbb C$; Liouville rules out a bijection from the whole plane onto the bounded disk. Nor does it say every annulus maps to a disk; an annulus is not simply connected. Boundary extension requires additional assumptions about the boundary and is not part of the bare theorem. Its proof uses tools beyond this core narrative, including normal families. The MIT 18.112 lecture notes listed below provide a route into that proof.

The six sections now form one chain. Complex differentiation restricts local behavior; Cauchy's formula turns that restriction into convergent series; Laurent coefficients identify singularities; residues turn singularities into contour integrals; and the argument principle turns those integrals into global counts. Conformal maps carry the same structure into geometry. Applications and computation can use this chain, but they also have to respect its hypotheses: the domain, its holes, the contour orientation, the location of singularities, and the branch of any multivalued function.

### Source note

The proof sequence, examples, and theorem formulations were checked against [MIT OpenCourseWare 18.04, *Complex Variables with Applications*, lecture notes](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/lecture-notes/) (especially Topics 1–5 and 7–11), [MIT OpenCourseWare 18.112, *Functions of a Complex Variable*, lecture notes](https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/resources/lecture-notes/) (especially Lectures 9–16 and 20), and the [UC Davis Math 185A complex-analysis course outline](https://www.math.ucdavis.edu/~hunter/m185a/m185a.html) for theorem scope and ordering. This draft uses its own exposition and worked examples.


## 7. Harmonic Functions and Applications


### A boundary-value problem made simple by a conformal map

Electrostatics gives a concrete reason to care that harmonic functions are the real and imaginary parts of holomorphic functions. In a charge-free region of a two-dimensional electrostatic problem, the potential $V(x,y)$ satisfies Laplace's equation,
$$
\nabla^2 V=V_{xx}+V_{yy}=0.
$$
If $V$ is the real part of a holomorphic function $F(z)=V(x,y)+iW(x,y)$, then $W$ is a harmonic conjugate. Its level curves cross the equipotentials $V=\text{constant}$ at right angles. The electric field is $\mathbf E=-\nabla V$. A conformal map can move a difficult region to a simpler one while preserving harmonicity and local angles; the boundary data must be transported along with the map.

There is a useful physical reading of the conjugate pair. The gradient of $V$ points normal to an equipotential. The Cauchy–Riemann equations make $\nabla W$ a ninety-degree rotation of $\nabla V$, so the two families of level curves intersect orthogonally wherever the derivative is nonzero. This does not mean that every physical boundary is an equipotential: it means that when a conductor is held at fixed potential, its surface is one member of that family. The conjugate function then supplies a convenient coordinate for the field lines.

In two dimensions, conformal invariance of Laplace's equation is the key transport rule. Let $z=g(\zeta)$ be a one-to-one holomorphic map on a region, with $g'(\zeta)\ne0$. If $V(z)$ is harmonic in the image region, then $\widetilde V(\zeta)=V(g(\zeta))$ is harmonic in the source region. In fact,
$$
\Delta_\zeta (V\circ g)=|g'(\zeta)|^2(\Delta_z V)\circ g.
$$
The map changes lengths by the local factor $|g'|$ and rotates directions by $\arg g'$, but it preserves angles and the zero of the Laplacian away from critical points. Boundary values travel by composition: if a source boundary point $\zeta$ maps to $z=g(\zeta)$, the value assigned at $z$ becomes the value at $\zeta$. Forgetting this correspondence is an easy way to solve the wrong boundary problem.

Consider an ideal conducting wedge with opening angle $\alpha$, with its two straight faces held at potentials 0 and $V_0$. Take polar coordinates with the wedge described by $r>0$ and $0<\theta<\alpha$. The map
$$
\zeta=z^{\pi/\alpha}
$$
sends the wedge to the upper half-plane. This power is defined using a chosen logarithm, $z^{\pi/\alpha}=\exp((\pi/\alpha)\operatorname{Log} z)$, with the branch of $\operatorname{Log}$ whose argument lies in $(0,\alpha)$ inside the wedge. Indeed, it multiplies arguments by $\pi/\alpha$, so $0<\arg z<\alpha$ becomes $0<\arg\zeta<\pi$. Positive points on the lower face map to the positive real axis; points on the upper face map to the negative real axis. The two electrodes therefore become the two halves of the real boundary, with the same constant values assigned to their corresponding points.

In polar coordinates $\zeta=\rho e^{i\vartheta}$, the angle function $\arg\zeta=\vartheta$ is harmonic in the upper half-plane away from its boundary singularities. It takes value 0 on the positive real axis and $\pi$ on the negative real axis. Scaling it by $V_0/\pi$ produces the desired boundary values:
$$
V(\zeta)=\frac{V_0}{\pi}\arg\zeta.
$$
Pulling this function back gives
$$
V(r,\theta)=\frac{V_0}{\alpha}\theta.
$$
This solution is independent of distance from the corner. Its field is not: in polar components,
$$
\mathbf E=-\nabla V=-\frac{V_0}{\alpha r}\,\mathbf e_\theta.
$$
The formula can be checked without trusting the mapping argument. In polar coordinates,
$$
\Delta V=V_{rr}+\frac1rV_r+\frac1{r^2}V_{\theta\theta}=0,
$$
because $V$ depends linearly on $\theta$ only. At $\theta=0$, it is 0; at $\theta=\alpha$, it is $V_0$. Its radial derivative is zero and its angular derivative is $V_0/\alpha$, giving the stated field. This direct check is valuable: mapping supplies a construction, while substituting into the differential equation and checking the boundary data verifies the result.

For a concrete right-angle wedge, set $\alpha=\pi/2$. Then $\zeta=z^2$, the potential is $2V_0\theta/\pi$, and the field magnitude is $2V_0/(\pi r)$. The map doubles every interior angle: the quadrant's boundary rays at angles 0 and $\pi/2$ become the two real rays at angles 0 and $\pi$. A boundary condition that was posed on a corner-shaped region has become the familiar angular potential in a half-plane. This example is especially helpful because it makes branch choice visible. If one uses a power without restricting the argument, the same point in the image plane may correspond to more than one preimage, and the proposed map is no longer a single-valued coordinate on the chosen region.

The boundary-value problem is also unique under the usual bounded-domain Dirichlet assumptions: two harmonic solutions with the same continuous boundary values have a harmonic difference that vanishes on the boundary, and the maximum principle forces that difference to vanish inside. The wedge is unbounded and has a corner, so one states the relevant boundedness or growth condition and treats the vertex separately; uniqueness does not follow merely from writing down a plausible harmonic function. The ideal solution above is the natural bounded angular solution on each annular truncation with compatible outer data, and is the standard local model near the corner.

The field's corner exponent has a useful interpretation beyond this one wedge. The inverse map is $z=\zeta^{\alpha/\pi}$, and its derivative has magnitude proportional to $|\zeta|^{\alpha/\pi-1}$. Uniform field in the mapped half-plane therefore becomes a field whose size scales like $r^{\pi/\alpha-1}$ in the wedge. For $\alpha=\pi/2$, this is $r^1$ for a uniform mapped field, while the particular angular-potential boundary data above produces $1/r$ because its mapped potential is an angle function with a boundary singularity at the origin. These are different mapped problems: the map alone does not determine the field; the transformed boundary data do. This distinction is a good safeguard against memorizing one corner exponent and applying it to every electrode arrangement.

The same exponential map gives a compact second geometry check. The infinite horizontal strip $0<\operatorname{Im}z<h$ maps to the upper half-plane under $\zeta=e^{\pi z/h}$. The lower edge maps to the positive real axis and the upper edge to the negative real axis. If those edges are held at 0 and $V_0$, respectively, then the half-plane angle potential pulls back to $V(x,y)=V_0y/h$: the familiar uniform field between parallel plates. This is a case where the answer is already easy in the original geometry, but the map makes the correspondence between strip boundaries and half-plane boundary pieces explicit. For finite plates, edge effects enter because the ideal infinite-strip boundary conditions no longer apply; the exponential map does not remove them.

In applied work, the useful question is often not “what is the map?” but “what boundary geometry becomes simple under a map I know?” Powers straighten wedges; exponentials straighten strips; Möbius maps move disks and half-planes while preserving circles and lines. Once a candidate is selected, check three things before solving: it is one-to-one on the region of interest, its derivative does not vanish in the interior, and each boundary segment maps to the boundary set on which the transformed data are actually known. A map that sends the domain correctly but scrambles which boundary values belong where is not a solution method.

The logarithm also connects potential theory to point sources. In a two-dimensional medium with constant conductivity, the potential of an ideal point source is proportional to $\log r$, where $r=|z|$. Since $\log|z|$ is harmonic away from the origin, it solves the source-free equation everywhere except at the source; integrating its radial derivative around a circle gives a nonzero total flux independent of the circle's radius. In distributional language, the Laplacian is concentrated at the origin. The complex function $\operatorname{Log} z=\log|z|+i\arg z$ packages the radial potential and angular conjugate, but the angle is multivalued globally. A branch cut makes the formula single-valued on a slit domain; it does not create a physical wall or remove the source. This is a useful distinction between a mathematical device for choosing a branch and a physical boundary in the field problem.

This logarithmic kernel is the two-dimensional analogue of the inverse-distance kernel in three dimensions and is a building block for Green's functions: kernels that encode how a point source contributes to a boundary-value problem. Boundaries modify the free-space kernel, often by adding a harmonic correction chosen to satisfy the boundary condition. That is the conceptual bridge from the elementary logarithm to more systematic potential theory. The detailed construction of Green's functions requires careful treatment of the domain and boundary regularity, so the connection here is a guide to further study rather than a general solution formula.

The idealized field diverges like $1/r$ at the vertex. That is a real feature of this mathematical boundary condition, but an actual electrode has a rounded tip, finite thickness, and material limits. The singularity warns that the ideal geometry predicts large local fields; it does not predict an infinite measurable field.

The example also shows why mapping is a method, not a magic eraser. The transformed boundary is easy, but the map has a branch point at the corner, and its derivative vanishes or diverges there depending on the angle. Away from that point the map is conformal; at the vertex the local angle-preservation argument does not apply. Boundary values on curved or segmented conductors are usually less tidy, and one may need an explicit map, a numerical map, or a numerical solution after mapping.

The same harmonic-conjugate structure describes ideal two-dimensional fluid flow. For an incompressible, irrotational velocity field in a simply connected fluid region, there is a velocity potential $\phi$ and a stream function $\psi$. With the convention
$$
F(z)=\phi(x,y)+i\psi(x,y),\qquad F'(z)=u-iv,
$$
the curves $\psi=\text{constant}$ are streamlines and $\phi=\text{constant}$ are equipotentials; the velocity is tangent to streamlines. For uniform flow of speed $U$ past a circular cylinder of radius $a$,
$$
F(z)=U\left(z+\frac{a^2}{z}\right),\qquad |z|>a.
$$
On $z=ae^{i\theta}$, the complex potential is $2Ua\cos\theta$, which is real, so the cylinder surface is a streamline. Differentiating gives $F'(z)=U(1-a^2/z^2)$; the two surface stagnation points occur at $z=\pm a$. This is an exact solution of the inviscid potential-flow model, not a model of viscous boundary layers, separation, or turbulent wake formation. MIT's notes develop complex potentials for two-dimensional hydrodynamics, while the University of Virginia notes work through electrostatic conformal maps and boundary problems ([MIT 18.04, hydrodynamics and complex potentials](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/mit18_04s18_topic6/); [University of Virginia, conformal mapping](https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_16_Conformal_Mapping.html)).

### A jump in boundary data

Suppose a harmonic potential $U(x,y)$ is prescribed on the real axis by
$$
U(x,0)=\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$
The value at $x=0$ is deliberately unspecified. A jump there prevents a continuous boundary extension, although a bounded harmonic solution exists in the upper half-plane. The Poisson integral for these data is the harmonic measure of the positive half-axis:
$$
U(x,y)=\frac1\pi\int_0^\infty
\frac{y}{(x-t)^2+y^2}\,dt,
\qquad y>0.
$$
Integrating with $s=(t-x)/y$ gives
$$
U(x,y)=\frac1\pi\left[\arctan s\right]_{-x/y}^{\infty}
=\frac12+\frac1\pi\arctan\frac{x}{y}.
$$
The quadrant and branch convention matter in interpreting the angle. For $z=x+iy$ in the upper half-plane, its argument $\theta=\arg z$ lies in $(0,\pi)$. Since $\arctan(x/y)$ takes values in $(-\pi/2,\pi/2)$,
$$
\arg z=\frac\pi2-\arctan\frac{x}{y},
\qquad
U(x,y)=1-\frac{\arg z}{\pi}.
$$
As $z$ approaches a positive real point from above, $\arg z\to0$ and $U\to1$. Approaching a negative real point gives $\arg z\to\pi$ and $U\to0$. At the jump point, limits depend on the approach direction, so no single boundary value makes the solution continuous there.

The Möbius map $w=(z-i)/(z+i)$ sends the upper half-plane to the unit disk and sends the real boundary to the unit circle. The point $z=0$, where the boundary data jump, maps to $w=-1$. What happens to the two boundary intervals? For real $x$,
$$
w(x)=\frac{x-i}{x+i},\qquad
\Im w(x)=\frac{-2x}{x^2+1}.
$$
Thus $x>0$ maps to the lower semicircle, while $x<0$ maps to the upper semicircle. The disk boundary data are therefore $1$ on the lower semicircle and $0$ on the upper semicircle, with a jump at $w=-1$ and another representation point at $w=1$ corresponding to $z=\infty$. Under this map the solution becomes
$$
\widetilde U(w)=1-\frac{1}{\pi}\arg\left(i\frac{1+w}{1-w}\right),
\qquad |w|<1,
$$
where the argument is chosen in $(0,\pi)$ for the inverse image in the upper half-plane. This expression is correct but not the most convenient disk formula. A geometric simplification comes from the harmonic measure of a semicircle: the disk solution is the angular fraction of the Poisson kernel over the lower semicircle. The Möbius map transports both the interior point and the boundary labels; simply declaring “lower half gets 1” without checking which real interval maps there would reverse the answer.

The map makes the boundary discontinuity visually simple, but it does not remove it. Near the two jump points on the circle, the solution changes rapidly. The Poisson integral remains bounded between zero and one, and its interior values are smooth. This is a useful distinction in applied work: a conformal change of coordinates can simplify geometry and preserve harmonicity, while the regularity of the boundary data remains a separate issue.

### A transform integral reduced to one residue

Residues can turn a real transform integral into a finite algebraic calculation. For $a>0$, evaluate
$$
I(a)=\int_{-\infty}^{\infty}\frac{e^{iax}}{x^2+1}\,dx.
$$
Close the real axis with a large semicircle in the upper half-plane. Since $|e^{iaz}|=e^{-a\operatorname{Im}z}\leq 1$ there, and the rational factor is $O(|z|^{-2})$, the arc integral tends to zero. The only enclosed pole is $z=i$, with residue
$$
\operatorname{Res}_{z=i}\frac{e^{iaz}}{z^2+1}
=\frac{e^{iai}}{2i}=\frac{e^{-a}}{2i}.
$$
The residue theorem yields $I(a)=2\pi i\,e^{-a}/(2i)=\pi e^{-a}$. Taking the real part gives the cosine transform; the imaginary part vanishes by oddness. For $a<0$, close in the lower half-plane instead, with clockwise orientation, and obtain $I(a)=\pi e^{-|a|}$. Thus
$$
\int_{-\infty}^{\infty}\frac{e^{iax}}{x^2+1}\,dx=\pi e^{-|a|}.
$$
The sign of $a$ determines the decaying half-plane. A frequent error is to keep the upper contour for negative $a$, where the exponential grows. The decay estimate and the contour orientation are part of the argument, not bookkeeping to omit.

Here are the hypotheses behind that calculation. The real integral is absolutely convergent because $(1+x^2)^{-1}$ is integrable and $|e^{iax}|=1$ for real $x$. For fixed $a>0$, take the contour consisting of the segment from $-R$ to $R$ and the upper semicircle, oriented counterclockwise. Its only pole is $i$, and no pole lies on the contour. On the semicircle, $|z^2+1|\geq ||z|^2-1|=R^2-1$, while $|e^{iaz}|=e^{-a\operatorname{Im}z}\leq1$. The arc length is $\pi R$, so the modulus of the arc integral is at most $\pi R/(R^2-1)$, which tends to zero. The residue theorem applies for every $R>1$; letting $R\to\infty$ gives the asserted improper integral. For $a=0$, the same formula follows directly from $\int (1+x^2)^{-1}dx=\pi$, or by continuity. For $a<0$, the lower semicircle gives exponential decay and clockwise orientation; its negative sign cancels the sign change in the residue contribution. No principal-value interpretation is needed because the integrand has no real pole.

This example is a Fourier transform under the convention $\widehat f(a)=\int_{\mathbb R}f(x)e^{iax}\,dx$. A different convention may put a minus sign in the exponential or a factor of $1/\sqrt{2\pi}$ in the definition, so transform tables cannot be compared until conventions match. The contour argument works because the rational decay beats the arc length and the exponential is non-growing in the chosen half-plane. In other problems, a slower-decaying rational function or an exponential that grows along part of the arc requires a different contour or a more refined estimate, such as Jordan's lemma.

### A bounded saddle-point example

The same contour ideas explain a basic asymptotic estimate. Let $\lambda>0$ grow and consider
$$
J(\lambda)=\int_{-\infty}^{\infty}e^{-\lambda x^2}\,dx.
$$
The dominant contribution comes from the unique minimum of $x^2$, at $x=0$. Rescale $y=\sqrt{\lambda}x$; then
$$
J(\lambda)=\lambda^{-1/2}\int_{-\infty}^{\infty}e^{-y^2}\,dy
=\sqrt{\frac{\pi}{\lambda}}.
$$
Here the “local quadratic approximation” is exact, so the leading saddle-point form $\sqrt{\pi/\lambda}$ has no correction terms. For a smooth phase $f(x)$ with a non-degenerate interior minimum at $x_0$, Laplace's method instead predicts a leading contribution proportional to
$$
e^{-\lambda f(x_0)}\sqrt{\frac{2\pi}{\lambda f''(x_0)}}.
$$
That estimate requires control of the rest of the integration domain and appropriate smoothness and growth assumptions; competing minima, endpoints, degenerate stationary points, and complex saddles change the analysis. The Gaussian example illustrates the scaling and normalization, not a universal recipe that can be applied by inspecting a plot. For broader asymptotic methods, the [NIST Digital Library of Mathematical Functions, §2](https://dlmf.nist.gov/2) gives a careful reference.

The mechanism is local concentration. If $f$ has a strict global minimum at $x_0$, then values away from $x_0$ carry an exponentially smaller factor $e^{-\lambda f(x)}$. Near the minimum, Taylor expansion gives
$$
f(x)=f(x_0)+\frac12 f''(x_0)(x-x_0)^2+O((x-x_0)^3).
$$
The contributing neighborhood has width of order $\lambda^{-1/2}$: set $x=x_0+y/\sqrt{\lambda}$. The exponent becomes $-\lambda f(x_0)-\tfrac12 f''(x_0)y^2+O(y^3/\sqrt{\lambda})$, and the differential contributes $dx=dy/\sqrt{\lambda}$. To leading order the remaining integral is a Gaussian. With a smooth amplitude $g$, this yields
$$
\int g(x)e^{-\lambda f(x)}\,dx \sim
g(x_0)e^{-\lambda f(x_0)}\sqrt{\frac{2\pi}{\lambda f''(x_0)}}.
$$
One standard sufficient setting is a real integral over a fixed interval or the real line, a unique interior global minimum, $f$ at least four times continuously differentiable near $x_0$, $f''(x_0)>0$, and a smooth amplitude with adequate integrability; outside every fixed neighborhood of $x_0$, assume the phase is separated from its minimum enough that the tail is exponentially smaller. Under routine stronger smoothness and tail conditions, the leading term has relative error $O(1/\lambda)$. If the amplitude vanishes at the minimum, the leading power changes. Equal-depth minima contribute a sum; a boundary minimum gives a different scaling; if $f''(x_0)=0$, the quadratic Gaussian model fails. This is the real Laplace method, closely related to saddle-point approximations. Complex contour steepest descent is a broader theory, and should not be inferred from this one real-variable estimate.


## 8. Computational Complex Analysis



Numerical work is most useful here as a way to inspect geometry, test a derivation, and find mistakes in signs or branches. It does not establish analyticity or prove that a contour encloses all singularities. Python is the canonical language in these examples. The arrays below represent a rectangular grid in the complex plane; the hue records argument and brightness records modulus.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.0, 2.0, 801)
y = np.linspace(-2.0, 2.0, 801)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Principal logarithm: the branch cut lies on the negative real axis.
F = np.log(Z)
phase = np.angle(F)
brightness = np.tanh(np.abs(F) / 3.0)

plt.imshow(
    phase, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower",
    cmap="twilight", vmin=-np.pi, vmax=np.pi,
)
plt.contour(X, Y, brightness, levels=np.linspace(0.1, 0.9, 9),
            colors="white", linewidths=0.35)
plt.axhline(0, color="black", linewidth=0.5)
plt.gca().set_aspect("equal")
plt.xlabel("Re z")
plt.ylabel("Im z")
plt.title("Domain coloring of the principal logarithm")
plt.show()
```

The picture should show a discontinuity across the negative real axis, the chosen branch cut. The origin is excluded because the logarithm is singular there. Grid coloring can make a jump look like a steep but continuous transition, and a finite plot cannot certify the location or nature of a singularity. NumPy defines complex `log` using the principal branch and documents its negative-real-axis cut; check the convention when comparing formulas or libraries ([NumPy `log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html)).

The code is intentionally explicit about the grid and the branch. `np.angle` returns values in $(-\pi,\pi]$, so hue wraps at the argument cut. Masking the origin avoids asking a floating-point routine to assign a finite logarithm to zero. The contour lines display levels of $|F|$, not additional phase information. A denser mesh can make the image smoother but cannot remove the branch discontinuity; changing the branch convention moves the cut and changes the displayed function while leaving its local derivative $1/z$ unchanged.

Here is a second, geometric visualization that directly uses the wedge map. It samples radial and angular lines in the quarter-plane and plots their images under $z\mapsto z^2$. The image should be a half-disk with straightened boundary rays. This is a plotting aid, not the solution of a new boundary-value problem.

```python
import numpy as np
import matplotlib.pyplot as plt

alpha = np.pi / 2
power = np.pi / alpha
radii = np.linspace(0.15, 1.0, 9)
angles = np.linspace(0.0, alpha, 9)
t = np.linspace(0.0, 1.0, 300)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
for r in radii:
    z = r * np.exp(1j * t * alpha)
    w = z**power
    axes[0].plot(z.real, z.imag, color="steelblue", linewidth=0.7)
    axes[1].plot(w.real, w.imag, color="steelblue", linewidth=0.7)
for theta in angles:
    z = t * np.exp(1j * theta)  # radial segments
    w = z**power
    axes[0].plot(z.real, z.imag, color="darkorange", linewidth=0.7)
    axes[1].plot(w.real, w.imag, color="darkorange", linewidth=0.7)

for ax, title in zip(axes, ["Right-angle wedge", "Image under z -> z^2"]):
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    ax.set_xlabel("real part")
    ax.set_ylabel("imaginary part")
    ax.set_title(title)
plt.tight_layout()
plt.show()
```

The radial lines remain radial while their angles double; the circular arcs remain circular but their radii become $r^2$. A numerical power operation on complex arrays uses the principal branch, which agrees with the selected branch on this quarter-plane. If the sampled angular interval crossed a branch cut, the same expression could produce a visually unexpected seam.

An idiomatic base R equivalent can display the phase of the principal logarithm without requiring a plotting package. It evaluates a regular grid, converts the phase to a cyclic hue, and uses `image()` to draw the raster. `outer()` constructs the matrix with one axis for each coordinate vector; R's `image()` convention expects `nrow(z) == length(x)` and `ncol(z) == length(y)`, which is why the matrix is passed without a transpose.

```r
x <- seq(-2, 2, length.out = 501)
y <- seq(-2, 2, length.out = 501)
z <- outer(x, 1i * y, `+`)
f <- log(z)
phase <- Arg(f)
phase[Mod(z) == 0] <- NA_real_

hue <- (phase + pi) / (2 * pi)
palette <- hcl(h = seq(0, 360, length.out = 257)[-257], c = 80, l = 55)
image(x, y, matrix(hue, nrow = length(x)), col = palette, zlim = c(0, 1),
      xlab = "Re z", ylab = "Im z", asp = 1,
      main = "Phase of the principal logarithm")
```

For a publication-quality or interactive figure, construct a stable color scale explicitly rather than relying on the set of colors present in each grid; the code emphasizes the complex-array operations and branch behavior. As in the Python plot, the hue seam reflects the principal argument convention, not a defect in the plotting library. The grid includes zero, where `log(0)` is not finite, so that point is masked after evaluation; warnings about the expected singular value can be avoided by excluding zero before taking the logarithm.

For a symbolic residue, SymPy can verify the local algebra:

```python
import sympy as sp

z, a = sp.symbols("z a", positive=True, real=True)
f = sp.exp(sp.I * a * z) / (z**2 + 1)
residue_at_i = sp.residue(f, z, sp.I)
print(sp.simplify(residue_at_i))  # -I*exp(-a)/2
```

This computes the residue at the requested point; it does not choose a contour, check whether other poles are enclosed, or justify a vanishing arc. Those are mathematical decisions outside the symbolic command.

For a numerical contour check, parameterize the circle $z(t)=Re^{it}$, so $dz=iRe^{it}dt$. The following integrates counterclockwise around $|z|=2$ and should return $2\pi i$ for $1/(z-i)$:

```python
import mpmath as mp

mp.mp.dps = 40
radius = mp.mpf("2")

def integrand_on_circle(t):
    z = radius * mp.e**(1j * t)
    dz_dt = 1j * radius * mp.e**(1j * t)
    return dz_dt / (z - 1j)

value = mp.quad(integrand_on_circle, [0, 2 * mp.pi])
print(value)
```

This block is self-contained once `mpmath` is installed. It evaluates one exact example with one simple pole and no near-boundary conditioning problem: the pole at $i$ is one unit from the circle. For a useful numerical diagnostic, compare the computed value with the theorem's prediction and then vary both precision and quadrature subdivision. If the answer changes with subdivisions but not precision, sampling is the likely limitation; if it changes with precision at a stable subdivision, rounding may matter. These checks help diagnose an implementation but do not certify an arbitrary integrand.

The orientation is encoded by increasing $t$; reversing the limits changes the sign. A pole on the path makes ordinary contour quadrature ill-posed, and a pole close to the path can make adaptive sampling unreliable. Split the parameter interval if the integrand changes rapidly, and compare with an analytic residue calculation. Increasing precision reduces rounding error, but it does not repair inadequate sampling or a wrong contour.

R has native complex arithmetic and is convenient for a compact contour computation. Here a midpoint sum approximates the same circle integral; vectorizing the parameter values makes the code idiomatic R, and `sum()` performs the quadrature accumulation.

```r
n <- 200000L
radius <- 2
t <- 2 * pi * (seq_len(n) - 0.5) / n
z <- radius * exp(1i * t)
dz_dt <- 1i * radius * exp(1i * t)
dt <- 2 * pi / n

value <- sum(dz_dt / (z - 1i)) * dt
print(value)  # approximately 0+6.283185i
```

This is a discretization, not an exact integral. Doubling `n` and checking convergence is a useful diagnostic; it still cannot certify that an unobserved singularity was handled correctly. R's `integrate()` is designed for real-valued integrands, so for complex line integrals split into real and imaginary parts and integrate each component, or use an explicit complex quadrature rule. See the [R `integrate` documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/integrate.html).

Several numerical traps recur across these examples. Principal arguments jump at branch cuts, so a sampled phase plot can create false discontinuities or hide a chosen branch. A contour that passes too close to a pole produces large, rapidly varying values; a coarse grid may miss the pole entirely. Finite differences near a singularity amplify cancellation, and a residue computation can be exact while its contour selection is wrong. Always state the parameterization and orientation, inspect the singularities analytically, refine the discretization, and distinguish precision error from discretization error. For conformal-map plots, draw a grid and its image, but remember that a coarse mesh can hide crowding near a boundary or a critical point where the derivative vanishes.

Machine precision is only one part of the error budget. In double precision, subtraction of nearly equal complex values can discard many significant digits, especially when evaluating a Laurent principal part near cancellation or comparing two close mapped coordinates. Scaling variables to order one, using a stable algebraic form, and checking with higher precision can expose this problem. Higher precision does not improve the mathematical conditioning of an ill-posed calculation: if a tiny perturbation in input causes a large change in the desired output, the model or formulation itself needs attention.

There is one more subtlety in computation: agreement between independent implementations is evidence of consistency, not proof. A symbolic residue and a numerical contour sum can share the same mistaken pole choice if both were copied from the same derivation. A reliable workflow checks the analytic hypotheses first, then uses a symbolic system for local algebra, and finally uses numerical quadrature to test orientation, parameterization, and scale. When the result is sensitive, report the contour, precision, discretization, and convergence behavior so someone else can reproduce the check.

When a computed contour integral fails to approach its expected value, change one numerical control at a time. First verify the parameterization algebraically, including its derivative and orientation. Then keep the path fixed and increase the number of quadrature nodes or subdivide the parameter interval near rapid variation. Separately increase arithmetic precision. Finally move the contour slightly, while keeping the same enclosed poles, to see whether a near-pole conditioning problem dominates. A correct residue integral is invariant under such a deformation as long as the integrand remains holomorphic in the region swept out. If the computed answer changes substantially under a harmless contour deformation, the discrepancy is evidence about numerical error or a singularity that was not accounted for. It is not evidence that residues depend on the contour's shape.

### Numerical margins for zero counts

For the argument principle, sample the image curve $f(z(t))$ and unwrap its phase. A net change close to $2\pi k$ suggests winding number $k$. But phase unwrapping assumes adjacent samples do not jump across an unresolved turn, and it becomes unstable if $f(z(t))$ approaches zero. Monitor the minimum sampled modulus as the mesh is refined. If it trends toward zero, the boundary may contain a zero or pass close to one; the theorem's nonvanishing boundary hypothesis is then numerically ill-conditioned. A reliable certified count needs a bound on the image between samples, interval arithmetic, or another validated method.

For a Rouché argument, the meaningful numerical quantity is the margin
$$
\delta=\min_{z\in C}\bigl(|f(z)|-|g(z)|\bigr).
$$
A positive certified lower bound proves strict dominance. A dense sample with positive values merely suggests it. If the minimum is small relative to floating-point error or interpolation error, the proposed split is fragile even if the exact inequality is true. Try a different contour or a different grouping of terms to increase the margin. This is the computational analogue of selecting a contour where the theorem has room to work.

Domain coloring and mapped grids are similarly diagnostic. A phase seam can be the chosen branch cut, an actual zero, or a plotting wrap from $\pi$ to $-\pi$; inspect the formula and the domain before interpreting colors. Grid crowding under a conformal map often signals a large derivative or a boundary point mapped near infinity, but a finite grid cannot measure an extremal distortion reliably. A vanishing derivative, as with $z^2$ at zero, is qualitatively different: local angle preservation fails there. Plot refinement can reveal a missed feature, but it cannot turn samples into a theorem.

### Source notes

- The wedge mapping and complex-potential framing follow the applied boundary-value and hydrodynamics treatments in [MIT OpenCourseWare 18.04, Topic 6](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/mit18_04s18_topic6/) and [University of Virginia, 2D electrostatics and conformal mapping](https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_14_2D_Electrostatics_Complex_Var_1.html).
- Complex logarithm branch behavior: [NumPy `log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html). Plotting approach: [Matplotlib `contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html).
- Symbolic residues: [SymPy residue documentation](https://docs.sympy.org/latest/modules/series/series.html#sympy.series.residues.residue). Numerical contour quadrature: [mpmath quadrature](https://mpmath.org/doc/current/calculus/integration.html).
- Real-valued numerical integration in R: [R `integrate`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/integrate.html). Asymptotic methods: [NIST DLMF, Chapter 2](https://dlmf.nist.gov/2).


## 9. Exercises, Outline Solutions, and Further Reading


These problems ask you to choose and justify a complex-analytic tool, not just execute a familiar formula. Unless stated otherwise, contours are positively oriented, zeros are counted with multiplicity, and a “domain” is open and connected. Give hypotheses and explain contour choices. Computations and plots are useful diagnostics, never proofs.

#### Exercises

#### Conceptual

1. A classmate claims that $f(z)=\overline z$ is complex differentiable at $0$, but nowhere else. Test the claim using the difference quotient. Explain what the Cauchy–Riemann equations can and cannot establish at a single point.
2. A student claims that $1/z$ has an antiderivative on $\mathbb C\setminus\{0\}$, since it is holomorphic there. Identify the error using a closed contour integral. Give a familiar topological condition on a domain that guarantees every holomorphic function has a primitive.
3. Let $u(x,y)=x^2-y^2$. Find every harmonic conjugate $v$ on a connected open set and express the resulting analytic functions. Contrast this with $u(x,y)=\log|z|$ on the punctured plane: identify local conjugates and explain the global obstruction.
4. Suppose $f$ is continuous on a region and its real and imaginary components have continuous first partial derivatives satisfying the Cauchy–Riemann equations. State what follows and why the regularity assumption matters. Give a counterexample to the claim that the equations at one point alone imply complex differentiability there.

#### Analytic

5. Classify the finite singularities of $f(z)=e^z/(z^2+1)$, and calculate both residues. Separately use a semicircular contour to evaluate
$$
\int_{-\infty}^{\infty}\frac{dx}{x^2+1}.
$$
State which function is integrated on the contour, which pole is enclosed, and why the arc contribution vanishes.
6. Find the Laurent series of $z/(z-1)$ about zero on $0<|z|<1$ and on $|z|>1$. Give the convergence region of each series and explain why the expansions differ even though they represent the same function wherever both expressions are defined.
7. Use Rouché’s theorem to count the zeros of $p(z)=z^5+3z+1$ in $|z|<1$, in $|z|<2$, and in $1<|z|<2$. Identify the comparison function on each circle and verify the strict inequality.
8. Find the residue of $g(z)=\exp(1/z)/z^2$ at zero and classify the singularity. Explain why a finite residue does not imply that the singularity is a pole.
9. Evaluate $\oint_{|z|=2} (z^2+1)/(z(z-1))\,dz$. Show how the answer follows from residues and also from the coefficient of $1/z$ in the Laurent expansion valid on the contour’s exterior annulus.
10. Apply the argument principle to $f(z)=z^2+1$ on $|z|=2$ and on $|z|=1/2$. Evaluate the change in argument of $f(z)$ around each circle and explain how it gives the zero count.

#### Geometric

11. Find a Möbius transformation mapping the upper half-plane to the unit disk and sending $i$ to $0$. Locate the images of $0,1,\infty$. Explain why the real axis maps to the unit circle and which side maps to its interior.
12. Describe the image of the strip $0<\operatorname{Re}z<1$ under $w=e^{\pi z}$. Is the map one-to-one? Describe the images of the two boundary lines and identify the period that determines how often they are covered.
13. Let $f$ be holomorphic near $z_0$ with $f'(z_0)\ne0$. Explain the local geometric meaning of conformality, including what happens to a small grid. Give an example showing that a conformal map need not be globally one-to-one on an arbitrary domain.
14. Let $u$ be harmonic on a bounded domain and continuous on its closure. State the maximum principle for $u$, and explain what it implies for a Dirichlet problem with specified boundary values. Why does this theorem not by itself construct the solution?

#### Applications

15. In two-dimensional incompressible, irrotational flow, take the complex potential $F(z)=Uz+a/z$, with real $U,a>0$, and complex velocity $F'(z)$. Find the stagnation points and derive the nontrivial streamline $\operatorname{Im}F=0$. Explain its physical interpretation and the idealisations behind the model.
16. A harmonic potential is prescribed on a simply connected domain whose boundary-value geometry is awkward. Explain how a conformal map can transfer the Dirichlet problem to a disk and back. State what is preserved, what is rescaled, and why the method does not automatically provide an explicit solution for every domain or boundary condition.
17. Consider $I(\lambda)=\int_{-\infty}^{\infty}e^{-\lambda x^2}\,dx$ for real $\lambda>0$. Explain how a standard real-variable argument obtains its value, and discuss what complex analysis contributes when the exponent or contour is generalized. Name one condition needed before moving a contour in a parameter-dependent integral.

#### Computational

18. Parameterise $\gamma_R(t)=Re^{it}$, $0\le t\le2\pi$, and approximate $\oint_{\gamma_R} dz/(z-1)$ by the periodic trapezoidal rule for $R=2$ and $R=1/2$, using $N=32,128,512$. Compare with the exact answers. Explain the distinct convergence behavior in terms of singularities and winding number.
19. Plot the principal logarithm on $[-2,2]^2$, masking a narrow band around the negative real axis and the origin. Show modulus and phase separately, mark the branch jump, then choose a simply connected subregion on which a continuous argument exists. Explain why increasing pixel resolution cannot remove the branch cut.
20. Use a computer algebra system to expand $\sin z/z^3$ at zero and compute its residue there. Compare the symbolic result with a hand derivation and identify what the software is taking as the expansion variable and center. State one reason a correct symbolic output could still mislead.

#### Outline solutions

1. At every point, the difference quotient of $\overline z$ is $\overline h/h$. Taking $h$ real gives $1$, while taking $h$ purely imaginary gives $-1$, so there is no limit. Equivalently, for $f=u+iv=x-iy$, CR fails everywhere. The equations are necessary for differentiability; satisfaction at one point is not generally sufficient. For a counterexample, define the real-valued function $f$ by $f(0)=0$ and
$$
f(x+iy)=\frac{x^2y}{x^4+y^2}\quad\text{when }(x,y)\ne(0,0).
$$
Both first partial derivatives at zero exist and are zero, so CR holds there. Along the path $y=x^2$, however, $f=1/2$, and $f(z)/z$ does not approach a finite limit. Continuously differentiable components satisfying CR on a neighbourhood do imply holomorphy.
2. A primitive would make every closed-curve integral zero, but the unit circle gives $\oint dz/z=2\pi i$. Holomorphy is local; simple connectivity is a standard sufficient condition for a primitive. More generally, all closed-curve integrals must vanish.
3. CR gives $v_y=2x$, $v_x=2y$, hence $v=2xy+C$ and $f(z)=z^2+iC$. For $u=\log|z|$, local conjugates are branches of $\arg z$. Continuation once around zero changes the argument by $2\pi$, so there is no globally single-valued conjugate on the punctured plane. The obstruction is topological, not a failure of local harmonicity.
4. Continuous first partial derivatives plus CR imply complex differentiability throughout the region. Continuity controls the first-order real differentiability remainder in the complex difference quotient. Without that regularity, pointwise equations do not control the remainder; the function in Exercise 1 has zero first partials at the origin but an unbounded difference quotient along $y=x^2$.
5. The simple poles of $e^z/(z^2+1)$ are $i,-i$. The residues are $e^i/(2i)$ and $-e^{-i}/(2i)$. For the real integral, instead integrate $1/(z^2+1)$ over the real segment and upper semicircle. Only $i$ is enclosed; its residue is $1/(2i)$, so the closed integral is $\pi$. On the arc $|z|=R$, the integrand is $O(R^{-2})$ and the arc length is $\pi R$; the arc integral is $O(R^{-1})\to0$. The two integrands in the question are deliberately different.
6. For $|z|<1$, $z/(z-1)=-z/(1-z)=-\sum_{n=1}^{\infty}z^n$. For $|z|>1$, $z/(z-1)=1/(1-1/z)=\sum_{n=0}^{\infty}z^{-n}$. The geometric series have distinct convergence regions separated by the pole at $1$. A Laurent expansion belongs to an annulus of analyticity, so the same center can support different expansions on different annuli.
7. On $|z|=1$, compare $3z$ with $z^5+1$: $|3z|=3$ and $|z^5+1|\le2$. Rouché gives one zero. On $|z|=2$, compare $z^5$ with $3z+1$: $|z^5|=32$ and $|3z+1|\le7$. Thus there are five zeros inside radius two and four in the annulus. The inequalities are strict on the complete boundary circles, so no boundary zeros complicate either count.
8. Expand $g(z)=\sum_{n=0}^{\infty}z^{-(n+2)}/n!$. No $z^{-1}$ term appears, so the residue is zero. Infinitely many negative powers occur, hence the singularity is essential. The residue is only one Laurent coefficient; it does not determine the rest of the principal part.
9. Partial fractions give $(z^2+1)/(z(z-1))=1-1/z+2/(z-1)$. The enclosed residues at zero and one are $-1$ and $2$, summing to $1$, so the integral is $2\pi i$. On $|z|>1$, expand $1/(z-1)=z^{-1}(1-z^{-1})^{-1}$; the coefficient of $z^{-1}$ in the full expression is $1$, giving the same answer. The coefficient method applies because the contour lies in that annulus.
10. On a positively oriented circle, the argument principle gives $N-P=(2\pi i)^{-1}\oint f'/f\,dz$, equivalently the net change in argument divided by $2\pi$. For $z^2+1$, both zeros $\pm i$ lie inside radius two and neither lies inside radius one-half; there are no poles. The change is therefore $4\pi$ on the larger circle and zero on the smaller. One can also see this geometrically: the image $z^2+1$ winds twice around zero for the larger circle and not at all for the smaller.
11. $w=(z-i)/(z+i)$ works. It sends $i\mapsto0$, $0\mapsto-1$, $1\mapsto-i$, and $\infty\mapsto1$. For real $x$, numerator and denominator have equal modulus, so the real axis maps to $|w|=1$. In the upper half-plane $|z-i|<|z+i|$, so the image lies inside the circle.
12. Since $|e^{\pi z}|=e^{\pi\operatorname{Re}z}$, the image is $1<|w|<e^\pi$. The map is not injective: $e^{\pi(z+2i)}=e^{\pi z}$, and both points remain in the strip. The lines $\operatorname{Re}z=0,1$ map to the unit circle and the circle of radius $e^\pi$, each covered repeatedly as the imaginary part varies.
13. The real Jacobian at $z_0$ is rotation and uniform scaling by $|f'(z_0)|$ to first order. Thus angles are preserved locally, and an orthogonal grid remains locally orthogonal, though its scale and orientation may vary with position. Yet $e^z$ is conformal everywhere and not injective on the whole plane because it has period $2\pi i$. Nonzero derivative gives local, not global, one-to-one behavior.
14. The maximum principle says a nonconstant harmonic function cannot attain an interior maximum or minimum. A continuous harmonic function on a bounded domain therefore takes its extrema on the boundary. This gives uniqueness for a Dirichlet problem: the difference of two solutions has zero boundary values and hence is identically zero. It does not prove existence or give a formula; those require separate construction or an existence theorem.
15. $F'(z)=U-a/z^2$, so the stagnation points are $z=\pm\sqrt{a/U}$. For $z=x+iy$, $\operatorname{Im}(a/z)=-ay/(x^2+y^2)$; hence $\operatorname{Im}F=y(U-a/(x^2+y^2))$. Besides the axis, the circle $x^2+y^2=a/U$ is a streamline passing through both stagnation points. It models uniform flow past a circular cylinder in ideal potential flow. The assumptions omit viscosity, turbulence, compressibility, and time dependence; the doublet singularity lies inside the excluded cylinder.
16. Let $\phi$ map the disk conformally to the physical domain. Composition $u\circ\phi$ is harmonic because the two-dimensional Laplacian transforms by $|\phi'|^2$. Dirichlet boundary values transfer by composition, and uniqueness transfers when the usual boundary hypotheses hold. Angles and harmonicity persist, while lengths and normal derivatives acquire scale factors. The Riemann mapping theorem supplies existence for proper simply connected domains, not an elementary formula; boundary regularity, multiply connected regions, and non-Dirichlet conditions require extra work.
17. Squaring the integral and using polar coordinates gives $I(\lambda)^2=\pi/\lambda$, and positivity selects $I(\lambda)=\sqrt{\pi/\lambda}$. Complex analysis helps with oscillatory or complex parameters, where contour deformation can expose decay or residues. A contour move requires holomorphy in the swept region (and accounting for any crossed poles); parameter limits also need domination or another interchange justification.
18. With $t_k=2\pi k/N$, use
$$
S_N=\frac{2\pi}{N}\sum_{k=0}^{N-1}
\frac{iR e^{it_k}}{Re^{it_k}-1}.
$$
The exact values are $2\pi i$ for $R=2$ and $0$ for $R=1/2$, by the residue theorem or winding number. In exact arithmetic, $S_N=2\pi i/(1-2^{-N})$ for $R=2$, while $S_N=-2\pi i\,2^{-N}/(1-2^{-N})$ for $R=1/2$. Both errors decay geometrically; for the smaller circle the finite sum is not exactly zero. The nearest singularity in the complexified parameter controls trapezoidal convergence. Refining the mesh never changes which pole is enclosed.
19. The principal logarithm has real part $\log|z|$ and imaginary part $\operatorname{Arg}z\in(-\pi,\pi]$. Its phase jumps across the negative real axis, while zero is a logarithmic singularity; mask both. Any simply connected region avoiding zero admits a continuous logarithm, possibly with a different argument interval. The jump expresses the inability to choose a global continuous argument around zero, so a finer grid can only sample it more sharply.
20. The expansion is $\sin z/z^3=z^{-2}-1/6+z^2/120-\cdots$. The singularity is a pole of order two and its residue, the coefficient of $z^{-1}$, is zero. A symbolic residue command takes a specified variable and center; check both, along with branch assumptions and simplifications. Correct output can still answer the wrong question if the point or variable was supplied incorrectly.

#### Further reading and references

#### Foundational texts and course notes

- **Accessible undergraduate text — Saff and Snider, *Fundamentals of Complex Analysis with Applications to Engineering and Science*, 3rd ed.** A readable first course with worked problems and engineering examples. Strong for contour integration, residues, and applications. [Pearson title page](https://www.pearson.com/en-us/subject-catalog/p/fundamentals-of-complex-analysis-with-applications-to-engineering-and-science/P200000003263/9780139078743).
- **Visual and geometric introduction — Tristan Needham, *Visual Complex Analysis*.** Builds intuition for conformal maps, harmonic functions, and the rigidity of analytic functions. Pair it with a theorem-oriented text when formal hypotheses matter. [Oxford Academic](https://global.oup.com/academic/product/visual-complex-analysis-9780198534464).
- **Classical rigorous text — Lars Ahlfors, *Complex Analysis*, 3rd ed.** Compact and proof-centered, with deeper treatment of analytic functions and conformal mapping than a first applied course. [McGraw Hill catalog](https://www.mheducation.com/highered/product/complex-analysis-ahlfors.html).
- **Broad undergraduate text — Marsden and Hoffman, *Basic Complex Analysis*, 3rd ed.** Balances core theory and geometry and extends beyond residue-calculus techniques. [Springer record](https://link.springer.com/book/10.1007/978-1-4612-0585-0).
- **Analytic viewpoint — Stein and Shakarchi, *Complex Analysis*, Princeton Lectures in Analysis II.** Connects one-variable theory to harmonic analysis and broader analytic ideas; a good next step after a first course. [Princeton University Press](https://press.princeton.edu/books/paperback/9780691113852/complex-analysis).
- **Free applied course — MIT OpenCourseWare 18.04, *Complex Variables with Applications*.** Topic-organized notes, problem sets, and solutions cover Cauchy theory, harmonic functions, hydrodynamics, residues, transforms, and conformal maps. [Lecture notes](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/lecture-notes/).
- **Free proof-focused notes — Dan Romik, UC Davis, *Complex Analysis*.** A compact sequence emphasizing precise theorem statements, residues, the argument principle, Rouché’s theorem, and introductory asymptotics. [PDF notes](https://www.math.ucdavis.edu/~romik/data/uploads/notes/complex-analysis.pdf).
- **Open textbook — Beck, Marchesi, Pixton, and Sabalka, *A First Course in Complex Analysis*.** A freely available, traditional undergraduate text for readers who want a complete course sequence with exercises. The Open Textbook Initiative lists it as an approved text; its first half covers analytic and harmonic functions and contour integration. [Book site](https://complexanalysis.org/) · [Open Textbook Initiative listing](https://textbooks-dev.aimath.org/textbooks/approved-textbooks/howell/).
- **Advanced classical text — J. B. Conway, *Functions of One Complex Variable I*, 2nd ed.** A systematic and proof-intensive treatment, including conformal mapping and the Riemann mapping theorem. [Springer record](https://link.springer.com/book/10.1007/978-1-4612-6313-5).

#### Applications and special topics

- **Potential flow — MIT OCW 18.04, Topic 6, “Two-Dimensional Hydrodynamics and Complex Potentials.”** Derives the connection between complex potential, velocity, streamlines, and flow around obstacles. Find the topic in the [course notes](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/lecture-notes/).
- **Boundary-value examples — P. Jeffrey, *Complex Analysis and Applications*, University of Newcastle notes.** Applied mathematical-methods material on boundary-value and mapping problems; consult the teaching page for the available notes. [Author’s teaching page](https://www.staff.ncl.ac.uk/p.j.jeffrey/).
- **Asymptotics and special functions — NIST Digital Library of Mathematical Functions, Chapter 2.** Authoritative formulas and references for Laplace’s method, stationary phase, steepest descent, and contour integrals. This is a technical reference rather than an introduction. [Asymptotic Approximations](https://dlmf.nist.gov/2).
- **Transforms and methods — Cambridge DAMTP, *Complex Methods*.** Course notes connect residues and contour choice to transforms and applied problems. [PDF](https://www.damtp.cam.ac.uk/user/examples/3P1.pdf).
- **Conformal mapping — Ahlfors and Conway (above).** Their treatments of Möbius transformations, boundary correspondence, and the Riemann mapping theorem provide a rigorous route beyond the canonical examples; existence alone does not give a convenient computational map.

#### History and context

- **History of analysis — Jeremy Gray, *The Real and the Complex: A History of Analysis in the 19th Century*.** Places complex function theory in the development of nineteenth-century analysis and its changing standards of rigor. [Springer record](https://link.springer.com/book/10.1007/978-3-319-23715-2).
- **Geometric context — Needham, *Visual Complex Analysis* (above).** Particularly effective for seeing how geometric interpretations illuminate the subject, though it is a mathematical exposition rather than a documentary history.

#### Software documentation

- **Arrays and branch conventions — NumPy, logarithms and complex routines.** Documents principal-value behavior and vectorized complex arithmetic; check results near branch cuts and signed zeros. [numpy.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html) · [Mathematical functions](https://numpy.org/doc/stable/reference/routines.math.html).
- **Plotting — Matplotlib contour and colormap normalization.** Useful for magnitude/phase plots and domain coloring. Use cyclic colors for phase and explicitly mask singularities and cuts. [contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html) · [Color normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html).
- **Symbolic expansions — SymPy series and residue functions.** Computes local series and Laurent coefficients; inspect variable, center, assumptions, and branch choices. [Series documentation](https://docs.sympy.org/latest/modules/series/series.html).
- **Arbitrary precision — mpmath integration.** Offers tanh-sinh and Gauss–Legendre quadrature. Extra precision cannot fix a contour crossing a singularity or a missed contribution. [Integration documentation](https://mpmath.org/doc/current/calculus/integration.html).
- **Adaptive quadrature — SciPy integrate.quad.** Integrates real-interval functions; for complex integrands, integrate real and imaginary parts separately and account for singularities and oscillation. [API reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html).
- **R complex arithmetic and integration — base and stats documentation.** Base R supports complex vectors; stats::integrate expects a real-valued function, so split complex integrals into real and imaginary components. [Complex numbers](https://stat.ethz.ch/R-manual/R-devel/library/base/html/complex.html) · [Integration](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/integrate.html).

#### Choosing a next step

For a first pass through the subject, pair the primer with MIT 18.04 or Saff and Snider: both keep applications visible while supplying additional worked examples. If a proof feels compressed, Romik’s notes give a more theorem-centered presentation; Ahlfors or Conway then provide a sustained rigorous development. Needham is the best fit when the algebra is familiar but the geometry of conformality, phase, or harmonic conjugates remains opaque.

The exercise set is intentionally mixed in difficulty. Problems 1–4 test definitions, hypotheses, and topology; 5–10 develop local expansions, residues, and global counting; 11–14 focus on maps and harmonic structure; 15–17 connect the theory to a physical or asymptotic model; and 18–20 ask you to treat computation as a controlled experiment. For a self-study pass, write a complete argument before consulting a solution sketch, then identify the exact theorem hypothesis that licenses each step. Where a sketch gives a result without a derivation, use the listed course notes or text to fill in the proof at the depth you need.

For potential theory, revisit the MIT complex-potential notes and then use a boundary-value text or course to learn how the analytic representation interacts with physical boundary conditions. The complex potential is a powerful reduction in two dimensions, but it does not encode viscous effects or remove the need to select physically valid boundary data. For asymptotic integrals, consult NIST DLMF only after identifying the relevant method and its hypotheses; the formulas are authoritative, but the presentation assumes mathematical maturity.

Software references answer API and convention questions, not theorem questions. When a symbolic package reports a residue, verify the Laurent coefficient and singularity classification by hand for at least one local expansion. When a quadrature routine disagrees with the residue theorem, first check orientation, poles on or near the contour, branch cuts, and whether the numerical path actually matches the intended contour. A plot is most useful as a way to discover a bad assumption or a missed feature, then return to the analytic argument.
