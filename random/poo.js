


function criaClasse(nome,atributos){

    let classObj = {
        [nome]: class {
            constructor(valores){
                for(let i=0 ; i < valores.length ; i++){
                    this[atributos[i]] = valores[i]
                }
            }
            show(){
                console.log(this)
            }

        }
    }
    return classObj[nome]
}


// let Pessoa_ = criaClasse('Pessoa',['idade','profissao','faculdade'])
// let eu_ = new Pessoa_([20,'programador','usp'])
// console.log(eu_)


function criaClasse2(nome,atributos,privateList=atributos.map(_=>true)){
    nome = nome.match(/["A-z"]/g).join('') 

    let privateAtributes = atributos.filter((_,i)=>privateList[i])
    let privateStr = ''
    let gettersStr = ''
    for(atr of privateAtributes){
        privateStr = privateStr.concat(`    #${atr} \n`)
        gettersStr = gettersStr.concat(`    get ${atr}(){\n        return this.#${atr}\n   }\n`) 
    }

    let constructorStr = ''
    for(atr of atributos){
        if(privateAtributes.includes(atr)){atrName = `#${atr}`}else{atrName = atr}
        constructorStr = constructorStr.concat(` 	this.${atrName} = ${atr} \n`)
    }    
    

    str = 
    `(\nclass ${nome}{\n` + 
    privateStr +
    `    constructor(${atributos.toString()}){ \n` +
    constructorStr +
    `   }\n`+
    gettersStr +
    `}\n)`


    console.log(str)

    let class_ = eval(str)
    return class_
}

// let Pessoa = criaClasse2("Pessoa{});\n throw new Error('ERRO');\n (class Pessoa",['nome','idade'],[false,true])
// let Pessoa = criaClasse2("Pessoa",['){}\n};\nthrow new Error("ERRO");\n function f(nome','idade'],[false,false])
let Pessoa = criaClasse2("Pessoa",['nome','idade'])
let eu = new Pessoa('lucas',19)
eu.nome = 'carlos'
console.log(eu.nome)
console.log(eu.idade)

