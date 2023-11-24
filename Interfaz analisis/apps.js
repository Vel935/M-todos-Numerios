


//funciones

function funcionEjem(x) {
    return ((x^2) - 4);
}
const myFunction = new Function('x', `return ${((x^2) - 4)};`);

function Biseccion(f,a,b,tol){
    if(f(a)*f(b)>0){
        console.log("La funcion f no cumple el teoreoma de valor intermedio, busque otro intervalo");
    }else{
        let c = a-((f(a)*(a-b))/(f(a)-f(b)))
        let i = 0
        while(Math.abs(f(c))>tol){
            let c = a-((f(a)*(a-b))/(f(a)-f(b)))
            if(f(a)*f(c)>0){
                a = c
            }else{
                b = c
            }
            i = i + 1
        }
        console.log("La raiz o el cero de la funcion usando falsa posicion es ", c);
        console.log("La cantidad de iteraciones en falsa posicion es", i);
    }
}


function runBiseccion(){
    let biseccionFun = document.getElementById("biseccionInput").value
    let biseccionA = document.getElementById("biseccionA").value
    let biseccionB = document.getElementById("biseccionB").value
    let biseccionTol = document.getElementById("biseccionTol").value
    let funcionBiseccion = new Function(`x`,`return ${biseccionFun}`)
    Biseccion(funcionBiseccion,biseccionA,biseccionB,biseccionTol)
}
Biseccion(myFunction,0,3,0.001)




function falsaPos(f,a,b,tol){
    if(f(a)*f(b)>0){
        console.log("La funcion f no cumple el teoreoma de valor intermedio, busque otro intervalo");
    }else{
        let i = 0
        while(Math.abs(b-a)>tol){
            let c = (a+b)/2
            if(f(a)*f(c)>0){
                a = c
            }else{
                b = c
            }
            i = i + 1
        }
        console.log("La raiz o el cero de la funcion usando falsa posicion es ", c);
        console.log("La cantidad de iteraciones en falsa posicion es", i);
    }
    return
}

function newtonR(f,x0,tol){
    let df = x =>{
        const h = 1e-10
        return (f(x+h)-f(x-h))/(2*h)
    }
    let newFun = x => x - f(x) / df(x)
    let x1 = newFun(x0)
    let i = 1
    while(Math.abs(x1 - xo) > tol){
        xo=x1
        x1=newFun(xo)
        i = i +1
    }
    console.log("La raíz de la función usando Newton es", x1)
    console.log("La cantidad de iteraciones usando Newton es", i)
    return
}

function Secante(f,x0,x1,tol){
    let x2 = x1-(f(x1)*(xo-x1)/(f(xo)-f(x1)))
    i = 1
    while(Math.abs(x2-x1) > tol){
        x0 = x1
        x1 = x2
        x2 = x1-(f(x1)*(xo-x1)/(f(xo)-f(x1)))
        i = i + 1
    }
    console.log("La raiz de la funcion usando Secante es", x2);
    console.log("El numero de iteraciones usandos Secante es", i);
    return
}

function poli_simple(xdata,ydata){
    const N = xdata.length
    P = []
    for(let i = 0; i<N ; i++){
        P.push([])
        P[i][0]=1
        for (let j = 1; j<N; j++){
            P[i][j] = P[i][j - 1] * xdata[i]
        }
    }
    const a_i = numeric.solve(M, ydata);
    let M = 0;
    for (let i = 0; i < N; i++){
        M += a_i[i] * Math.pow(x, i);
    }
    console.log("El polinomio interpolante es P(x) =", M);
    return x => {
        let result = 0;
        for (let i = 0; i < N; i++) {
            result += a_i[i] * Math.pow(x, i);
        }
        return result;
    };
}

function pol_lagrange(xdata, ydata) {
    const N = xdata.length;
    let P = 0;
    for (let i = 0; i < N; i++) {
        let T = 1;
        for (let j = 0; j < N; j++) {
            if (j !== i) {
                T *= (x - xdata[j]) / (xdata[i] - xdata[j]);
            }
        }
        P += T * ydata[i];
    }

    console.log("El polinomio es P(x) =", P);

    return x => {
        let result = 0;
        for (let i = 0; i < N; i++) {
            let T = 1;
            for (let j = 0; j < N; j++) {
                if (j !== i) {
                    T *= (x - xdata[j]) / (xdata[i] - xdata[j]);
                }
            }
            result += T * ydata[i];
        }
        return result;
    };
}

function Min_Cua(xd, yd) {
    const m = xd.length;
    const x = Symbol('x');
    const Sy = yd.reduce((acc, val) => acc + val, 0);
    const Sx = xd.reduce((acc, val) => acc + val, 0);
    const Sx2 = Sx**2;
    const Sxy = xd.reduce((acc, val, index) => acc + val * yd[index], 0);
    const Scx = xd.reduce((acc, val) => acc + val**2, 0);
    const a0 = ((Sy * Scx) - (Sx * Sxy)) / ((m * Scx) - Sx2);
    const a1 = ((m * Sxy) - (Sx * Sy)) / ((m * Scx) - Sx2);
    const P = a0 + a1 * x;
    console.log(P);
    return xValue => a0 + a1 * xValue;
}

function Euler(f, a, b, h, co) {
    const n = Math.floor((b - a) / h);
    const t = Array.from({ length: n + 1 }, (_, i) => a + i * h);
    const eu = [co];
    for (let i = 0; i < n; i++) {
        eu.push(eu[i] + h * f(t[i], eu[i]));
    }
    return { t, eu };
}

function Runge(f, a, b, h, co) {
    const n = Math.floor((b - a) / h);
    const t = Array.from({ length: n + 1 }, (_, i) => a + i * h);
    const rk = [co];
    for (let i = 0; i < n; i++) {
        const k1 = h * f(t[i], rk[i]);
        const k2 = h * f(t[i] + h / 2, rk[i] + 1 / 2 * k1);
        const k3 = h * f(t[i] + h / 2, rk[i] + 1 / 2 * k2);
        const k4 = h * f(t[i + 1], rk[i] + k3);
        rk.push(rk[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4));
    }

    return { t, rk };
}

function EulerO2(f, g, a, b, h, co1, co2) {
    const n = Math.floor((b - a) / h);
    const t = Array.from({ length: n + 1 }, (_, i) => a + i * h);
    const y = [co1];
    const v = [co2];
    for (let i = 0; i < n; i++) {
        const fy = h * g(t[i], y[i], v[i]);
        const fv = h * f(t[i], y[i], v[i]);
        y.push(y[i] + fy);
        v.push(v[i] + fv);
    }
    return { t, y, v };
}

function RungeO2(f, g, a, b, h, co1, co2) {
    const n = Math.floor((b - a) / h);
    const t = Array.from({ length: n + 1 }, (_, i) => a + i * h);
    const y = [co1];
    const v = [co2];
    for (let i = 0; i < n; i++) {
        const k1y = h * g(t[i], y[i], v[i]);
        const k1v = h * f(t[i], y[i], v[i]);
        const k2y = h * g(t[i] + h / 2, y[i] + 1 / 2 * k1y, v[i] + 1 / 2 * k1v);
        const k2v = h * f(t[i] + h / 2, y[i] + 1 / 2 * k1y, v[i] + 1 / 2 * k1v);
        const k3y = h * g(t[i] + h / 2, y[i] + 1 / 2 * k2y, v[i] + 1 / 2 * k2v);
        const k3v = h * f(t[i] + h / 2, y[i] + 1 / 2 * k2y, v[i] + 1 / 2 * k2v);
        const k4y = h * g(t[i] + h, y[i] + k3y, v[i] + k3v);
        const k4v = h * f(t[i] + h, y[i] + k3y, v[i] + k3v);
        y.push(y[i] + 1 / 6 * (k1y + 2 * k2y + 2 * k3y + k4y));
        v.push(v[i] + 1 / 6 * (k1v + 2 * k2v + 2 * k3v + k4v));
    }
    return { t, y, v };
}



function Trapecio(f, a, b, n) {
    const h = (b - a) / n;
    let S = 0;
    for (let i = 1; i < n; i++) {
        S += f(a + i * h);
    }
    const Int = (h / 2) * (f(a) + 2 * S + f(b));
    console.log("La integral por trapecio es ", Int);
    return Int;
}

function sims13(f, a, b, n) {
    if (n % 2 === 0) {
        let sp = 0;
        let si = 0;
        const h = (b - a) / n;
        for (let i = 1; i < n; i++) {
            if (i % 2 === 0) {
                sp += f(a + i * h);
            } else {
                si += f(a + i * h);
            }
        }
        const Int = (h / 3) * (f(a) + 4 * si + 2 * sp + f(b));
        console.log("La integral por medio de Simpson 1/3 es", Int);
    } else {
        console.log("No se puede calcular la integral por este método, n debe ser par");
    }
}

function sims38(f, a, b, n) {
    if (n % 3 === 0) {
        let mul = 0;
        let nomul = 0;
        const h = (b - a) / n;
        for (let i = 1; i < n; i++) {
            if (i % 3 === 0) {
                mul += f(a + i * h);
            } else {
                nomul += f(a + i * h);
            }
        }
        const Int = (3 * h / 8) * (f(a) + 2 * mul + 3 * nomul + f(b));
        console.log("La integral por medio de Simpson 3/8 es", Int);
    } else {
        console.log("No se puede calcular la integral por este método, n debe ser múltiplo de 3");
    }
}



