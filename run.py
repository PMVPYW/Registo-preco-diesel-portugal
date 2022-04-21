from sys import path
path.append('BP/')
import BP
path.append('Repsol/')
import Repsol
path.append('Galp/')
import Galp
path.append('Shell/')
import Shell
path.append('Alves Bandeira/')
import Alves_Bandeira
path.append('Cepsa/')
import Cepsa
path.append('Prio/')
import Prio
path.append('Rede Energia/')
import Rede_Energia
path.append('Pingo Doce/')
import Pingo_Doce
path.append('Intermarche/')
import Intermarche
import graph

BP.main()
Repsol.main()
Galp.main()
Shell.main()
Alves_Bandeira.main()
Cepsa.main()
Prio.main()
Rede_Energia.main()
Pingo_Doce.main()
Intermarche.main()

graph.graph()

begin_html = """

<!DOCTYPE html>
<html lang='pt'>
    <head>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <title>Preço gasóleo</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>
        <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p' crossorigin='anonymous'></script>
        <link rel="stylesheet" href="site.css">
    </head>
    <body>
        <div class="container">
            <div class="text-center">
                <img src="../graph.png" alt="graph">
            </div>
        </div>
        <br>
        <div class="text-center container">
            <div class="row">"""

end_html = """
            </div>
        </div>
    </body>
</html>"""

middle_html = ""

storaged={}
leist = []

with open("brands.txt", "r") as f:
    brands = f.read().split("\n")
for x in brands:
    price = graph.read(x)
    print(price, x)
    price = price[len(price)-1]
    storaged[price] = x
    leist.append(price)
    middle_html += f"""<div class="col-sm-4">
                <div class="card">
                    <div class="card-header">
                        <h1>{x}</h1>
                    </div>
                    <div class="card-body">
                        <h1>{price}&#8364</h1>
                    </div>
                </div>
            </div>"""
best = sorted(leist)[0]
print(f"best= {best}")
best = f"""<div class="col-sm-12    ">
                <div class="card">
                    <div class="card-header">
                        <h1>Melhor: {storaged[best]}</h1>
                    </div>
                    <div class="card-body">
                        <h1>{best}&#8364</h1>
                    </div>
                </div>
            </div>"""

with open("site/index.html", "w") as f:
    f.write(begin_html + best + middle_html + end_html)

import webbrowser

webbrowser.open_new("D:/OneDrive - IPLeiria/diesel project/site/index.html")