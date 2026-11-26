# Matched descriptive GLMs on frozen penguins and package-derived salamanders.
using LinearAlgebra, SHA, Printf
function readrows(path, expected)
    bytes=read(path); @assert bytes2hex(sha256(bytes)) == expected
    lines=split(chomp(String(bytes)), '\n'); header=replace.(split(lines[1], ','), '"'=>"")
    # These pinned inputs contain simple unescaped fields; reject unexpected column counts.
    rows=Dict{String,String}[]
    for line in lines[2:end]
        fields=replace.(split(line, ','), '"'=>""); @assert length(fields)==length(header)
        push!(rows,Dict(header .=> fields))
    end
    rows
end
function fit(X,y,family)
    b=zeros(size(X,2)); b[1]=log(sum(y)/length(y))
    for i in 1:300
        eta=X*b; mu=exp.(eta); weight=family==:poisson ? mu : ones(length(y))
        work=eta+(y-mu)./mu; updated=(X'*(weight.*X))\(X'*(weight.*work))
        if maximum(abs.(updated-b))<1e-11; return updated; end
        b=updated
    end
    error("$family did not converge")
end
penguins=readrows("data/penguins.csv","f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93")
p=filter(r->!(r["body_mass_g"] in ("NA", "")) && !(r["species"] in ("NA", "")),penguins)
@assert length(penguins)==344 && length(p)==342
y=[parse(Float64,r["body_mass_g"]) for r in p]; @assert all(y.>0)
c=Float64[r["species"]=="Chinstrap" for r in p]; g=Float64[r["species"]=="Gentoo" for r in p]
d=Float64[r["island"]=="Dream" for r in p]; t=Float64[r["island"]=="Torgersen" for r in p]
X=hcat(ones(length(p)),c,g); additive=hcat(X,d,t); interaction=hcat(additive,c.*d,c.*t,g.*d,g.*t)
@assert rank(additive)==5 && rank(interaction)==5 && size(interaction,2)==9
P=[1. 0 0; 1 1 0; 1 0 1]; gaussian=P*(X\y); gamma=exp.(P*fit(X,y,:gamma))
reference=[3700.66225165563,3733.08823529412,5076.0162601626]
@assert maximum(abs.(gaussian-reference))<1e-5 && maximum(abs.(gamma-reference))<1e-5
println("penguins n ",length(p)," additive rank ",rank(additive)," interaction rank/columns ",rank(interaction),"/",size(interaction,2))
println("gaussian means ",gaussian," gamma means ",gamma," Gentoo minus Adelie ",gaussian[3]-gaussian[1]," Gamma mean ratio ",gamma[3]/gamma[1])
sal=readrows("data/salamanders-package.csv","1dadca43a8c917da58cd341fb04f15c0ad22384a8487a33dc3f6b77516bf8874"); sm=filter(r->r["spp"]=="GP",sal)
sites=unique([r["site"] for r in sm]); @assert length(sal)==644 && length(sm)==92 && length(sites)==23
@assert all(count(r->r["site"]==site,sm)==4 for site in sites)
X=hcat(ones(length(sm)), Float64[r["mined"]=="yes" for r in sm], [parse(Float64,r["DOP"]) for r in sm]); y=[parse(Float64,r["count"]) for r in sm]
@assert rank(X)==3 && all(y.>=0)
b=fit(X,y,:poisson); predicted=exp.([1. 0 0; 1 1 0]*b)
@assert maximum(abs.(predicted-[2.20610650201214,0.045503366405712]))<1e-6
println("salamanders GP n ",length(sm)," sites ",length(sites)," poisson coefficients ",b," DOP 0 predicted counts ",predicted)
