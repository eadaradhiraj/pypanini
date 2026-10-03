from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()
res, _ = te.derive("ji", lakara="lw", purusha="prathama", vacana="eka", prayoga="kartari", dhatu_id="01.1096")
print(res)
