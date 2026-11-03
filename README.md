# Skarbnik – blog em polonês (finanças e impostos)

Site estático pronto para a Vercel. A pasta `public/` já está gerada.

## Publicar na Vercel
1. Suba esta pasta para um repositório GitHub (ou use a CLI `vercel` dentro da pasta).
2. Na Vercel: Add New > Project > importe o repo. Framework: "Other". Output Directory: `public`. Sem build command.
3. Ligue o seu domínio.

## Antes de publicar, edite em `build.py` e rode `python3 build.py`
- `SITE_URL`: o seu domínio real (canonical e sitemap)
- `ADSENSE`: o seu ID `ca-pub-XXXXXXXXXXXXXXXX` (depois de aprovado); troque também `SEU_SLOT` pelo ID do bloco de anúncio
- Email na página "Kontakt": o seu email real
- Novos artigos: adicione um item na lista `A` e rode o script de novo

## Notas
- Registe o site no Google Search Console e envie `/sitemap.xml`.
- Para AdSense na UE é obrigatório um banner de consentimento (CMP certificado).
- O AdSense costuma exigir bastante conteúdo original. Estes 5 artigos são a base: peça revisão a um falante nativo e confirme valores e limites em gov.pl antes de publicar.
