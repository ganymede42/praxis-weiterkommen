# praxis-weiterkommen

# Configure Hostfactory DNS for GitHub Pages

You want your domain registered at HOSTFACTORY to open the website hosted on GitHub Pages, while avoiding extra hosting or SSL costs.

The important part is to change the DNS records, not the nameservers. HOSTFACTORY's DNS management is available in your customer centre.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://support.hostfactory.ch\&sz=32)

HOSTFACTORY®

# 03.11.2026 09:20:34
```
https://my.hostfactory.ch/
-> Domainregistrationen -> praxis-weiterkommen.ch -> DNS verwalten
   -> Mehr -> DNS Aliases -> alle löschen
   -> Mehr -> Auf Standard zurücksetzen -> Publizieren
```

# 03.11.2026 09:46:01
```
Hugo vs WorldPress

Hugo:
apt update
apt install git
snap install hugo

WorldPress 
apt install  apache2  mariadb-server  php  libapache2-mod-php  php-mysql  php-curl  php-gd  php-intl  php-mbstring  php-xml  php-zip php-imagick

systemctl enable --now apache2
systemctl enable --now mariadb

-> Hugo is very lightweight and looks quickly nice -> good for our needs
```

03.11.2026 Hugo
```
cd /tmp
URL=$(python3 -c '
import json, urllib.request
d = json.load(urllib.request.urlopen(
    "https://api.github.com/repos/gohugoio/hugo/releases/latest"))
print(next(a["browser_download_url"] for a in d["assets"]
    if a["name"].startswith("hugo_extended_")
    and a["name"].endswith("_linux-amd64.deb")))
')
echo $URL
wget "$URL" -O hugo_extended.deb
sudo apt install ./hugo_extended.deb
which hugo
type -a hugo

https://chatgpt.com/c/6ae99c7e-f120-83ed-a612-7f39ec4e6f1a

hugo new site  praxis-weiterkommen
cd praxis-weiterkommen/

git submodule add --depth 1 https://github.com/gohugo-ananke/ananke themes/ananke

#clone origin:
mkdir _orig
cd _orig/
wget  --mirror  --convert-links  --adjust-extension  --page-requisites  --wait=1  --domains=praxis-weiterkommen.com  --no-parent https://www.praxis-weiterkommen.com/

cp _orig/md/english-1/profile/index.md content/_index.en.md
cp _orig/md/deutsch/profil/index.md content/_index.md
cp _orig/md/english-1/supply/index.md content/angebot.en.md
cp _orig/md/deutsch/angebot/index.md content/angebot.md
cp _orig/md/english-1/contact/index.md content/kontakt.en.md
cp _orig/md/deutsch/kontakt/index.md content/kontakt.md
cp _orig/md/counseling-in-crisis-situations/fees/index.md content/kosten.en.md
cp _orig/md/deutsch/kosten/index.md content/kosten.md
cp _orig/md/about/index.md content/profil.en.md

hugo server --noHTTPCache  --openBrowser
#xdg-open http://localhost:1313/

hugo --minify

Useful documentation:

- [Hugo – Getting Started](https://gohugo.io/getting-started/?utm_source=chatgpt.com)
- [Hugo – Multilingual websites](https://gohugo.io/content-management/multilingual/?utm_source=chatgpt.com)
- [Ananke documentation](https://gohugo-ananke.github.io/documentation/?utm_source=chatgpt.com)

/net/192.168.1.76/volume1/DS218_NAS/Monika/Documents/Praxis/

https://fducat18.github.io/hugo-air-demo/
https://fducat18.github.io/hugo-air-demo/en/
```

## 1. Open your DNS settings at HOSTFACTORY

[Jetzt .ch Domainregistrationen für fünf Franken](https://images.openai.com/static-rsc-4/v31ilwNEeC27BHSmzDWiAf9QM5cYhszYJYQXAf-_3b-SKLq5NjVyq5raFIi3XJncW2OWyQ2kYz-Y3VIWQ7QZzeC1op-MiCMn0vjjBsY0UbjMVWLqD4dH2njykmMS0lrCcs3ez3qFS67Jo42fvS9PWO0zi6j43dGGFonMXNTCltA?purpose=inline)

Step 1 — Sign in

Open [my.hostfactory.ch](https://my.hostfactory.ch/?utm_source=chatgpt.com) and sign in.

Step 2 — Select your domain

Open Domainregistrationen, select your `.ch` domain, then click DNS verwalten.

Step 3 — Review existing records

You should see a list of DNS records with types such as `A`, `AAAA`, `CNAME`, `MX` and `TXT`. You can add, edit and delete records here.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://support.hostfactory.ch\&sz=32)

HOSTFACTORY®

## 2. Add the DNS records for GitHub Pages

First, in your GitHub repository, go to Settings → Pages → Custom domain, enter your actual `.ch` domain (for example, `example.ch`), and click Save. GitHub recommends doing this before configuring DNS.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.github.com\&sz=32)

GitHub Docs

Now return to HOSTFACTORY and create or edit these records.

### A records — your main domain

Add four `A` records. Each one has the same host but a different IP address.

| Type | Hostname              | Value / destination |
| ---- | --------------------- | ------------------- |
| A    | `@` or blank for root | `185.199.108.153`   |
| A    | `@` or blank for root | `185.199.109.153`   |
| A    | `@` or blank for root | `185.199.110.153`   |
| A    | `@` or blank for root | `185.199.111.153`   |

HOSTFACTORY's interface may represent the root domain with an empty hostname rather than `@`. Use whichever form its DNS editor accepts for the domain itself.

These are GitHub's official IPv4 addresses.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.github.com\&sz=32)

GitHub Docs

### CNAME record — the `www` address

Add or edit one record for `www`.

| Field       | Value                      |
| ----------- | -------------------------- |
| Type        | `CNAME`                    |
| Hostname    | `www`                      |
| Destination | `YOUR-USERNAME.github.io.` |
| TTL         | Leave at default           |

Replace `YOUR-USERNAME` with your exact GitHub username. Keep the final dot in the destination when entering it at HOSTFACTORY, because HOSTFACTORY recommends a trailing dot for external DNS targets.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://support.hostfactory.ch\&sz=32)

HOSTFACTORY®

+1

For example, if your GitHub username were `mywebsite`, the destination would be `mywebsite.github.io.`

## 3. Check existing records before saving

This is important if you previously used Jimdo or have email configured.

- Edit or replace existing root-domain `A` records that point to the old website.
- Remove existing root-domain `AAAA` records pointing to the old hosting provider, unless you replace them with GitHub's IPv6 addresses below.
- Replace the existing `www` record if it conflicts with the new CNAME.
- Keep your `MX`, email-related `TXT`, SPF, DKIM and DMARC records. Do not delete the entire DNS zone or click Auf Standard zurücksetzen.

HOSTFACTORY warns that resetting the zone deletes custom records, including mail-related records.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://support.hostfactory.ch\&sz=32)

HOSTFACTORY®

Optional: for IPv6 support, you can also add these four `AAAA` records for the root domain:

| Type | Hostname              | Value                 |
| ---- | --------------------- | --------------------- |
| AAAA | `@` or blank for root | `2606:50c0:8000::153` |
| AAAA | `@` or blank for root | `2606:50c0:8001::153` |
| AAAA | `@` or blank for root | `2606:50c0:8002::153` |
| AAAA | `@` or blank for root | `2606:50c0:8003::153` |

Only replace the old IPv6 records if you want to configure GitHub's IPv6 support.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.github.com\&sz=32)

GitHub Docs

## 4. Publish and verify

1. Save the records in HOSTFACTORY.
2. If you see a Publizieren button, click it.
3. Wait for DNS changes to propagate. This can take up to 24 hours.
4. Return to GitHub → Settings → Pages. Wait for the domain check and HTTPS certificate setup to complete.
5. Enable Enforce HTTPS when the option becomes available.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://support.hostfactory.ch\&sz=32)

   HOSTFACTORY®

   +1

On your Ubuntu computer, you can check the records in a terminal:

```
dig +short A yourdomain.ch
dig +short CNAME www.yourdomain.ch
```

Replace `yourdomain.ch` with your real domain. The first command should return the four GitHub IPv4 addresses; the second should return your GitHub Pages hostname.

If you send me a screenshot of your HOSTFACTORY DNS record list (you can obscure your customer number and other private details), I can tell you exactly which records to edit, add or preserve.

https://my.hostfactory.ch/webhostings/
-> click on praxis-weiterkommen.ch 
-> click on DNS verwalten

add following entries:

| Type  | Hostname  | Value / destination       |
| ----- | --------- | --------------------------|
| A     | <blank>   | `185.199.108.153`         |
| A     | <blank>   | `185.199.109.153`         |
| A     | <blank>   | `185.199.110.153`         |
| A     | <blank>   | `185.199.111.153`         |
| CNAME | `git`     | `ganymede42.github.io.`   |

```
dig +short A praxis-weiterkommen.ch
dig +short CNAME git.praxis-weiterkommen.ch

dig +short A praxis-weiterkommen.ch           # 185.117.170.92
dig +short CNAME www.praxis-weiterkommen.ch   # praxis-weiterkommen.ch.
dig +short CNAME git.praxis-weiterkommen.ch   # ganymede42.github.io.
dig +short A mail.praxis-weiterkommen.ch      # 185.117.170.90
```

# Hints Hostfactory:
```

Für eine rein statische Website ist "GitHub Pages" in der Tat eine kostenlose Alternative.
Besten Dank, dass Sie die Domainregistration bei HOSTFACTORY® belassen!

Für die Umstellung im DNS drei Hinweise, an welchen es erfahrungsgemäss hakt:
 - Für die Hauptdomain praxis-weiterkommen.ch lässt sich kein CNAME setzen
   (gem. RFC 1034 nicht neben den übrigen Records zulässig).
   Richten Sie stattdessen via https://my.hostfactory.ch/ → "Domainregistrationen" → (Domainregistration auswählen) 
   → "DNS verwalten" → "Mehr" → "DNS Alias" → "Alias erstellen" einen HOSTFACTORY® DNS Alias auf Ihren Hostnamen bei
   "GitHub" (in der Form benutzername.github.io) ein; er ersetzt die bestehenden A- und AAAA-Records und führt die
   Adressen von "GitHub" automatisch nach. 
   alias: ganymede42.github.io

   (https://ganymede42.github.io/praxis-weiterkommen/)

 - Für www.praxis-weiterkommen.ch ändern Sie unter → "DNS verwalten" den bestehenden CNAME auf denselben Hostnamen 
   - mit abschliessendem Punkt (benutzername.github.io.), sonst wird der Wert relativ zur Zone verwaltet.

 - Bei "GitHub" muss die Domain als "Custom Domain" hinterlegt sein; das Zertifikat stellt "GitHub" erst aus, wenn 
   die Domain dorthin auflöst, was einige Stunden dauern kann._

 - Sollten Sie das Budget Webhosting "TINY" danach nicht mehr benötigen, hängen Sie die DNS-Zone vor dessen Ablauf via
   → "DNS verwalten" → "Zonenzuweisung" → "Zuweisung ändern" an die Domainregistration um - andernfalls fällt die Auflösung
   Ihrer Domain mit dem Abonnement weg.

 Sollten Sie es sich anders überlegen, würde es uns sehr freuen, Ihre Website künftig wieder in der Schweiz bei HOSTFACTORY® betreuen zu dürfen.

 Für weitere Fragen stehen wir Ihnen gerne zur Verfügung.
```

------------------

# chatgpt
---

Yes. A DNS name can have multiple `A` records, and that is exactly what GitHub Pages requires for a root domain such as `praxis-weiterkommen.ch`.

You should configure these four records at HOSTFACTORY:

| Type | Name                | IPv4 address      |
| ---- | ------------------- | ----------------- |
| A    | `@` (or root/blank) | `185.199.108.153` |
| A    | `@` (or root/blank) | `185.199.109.153` |
| A    | `@` (or root/blank) | `185.199.110.153` |
| A    | `@` (or root/blank) | `185.199.111.153` |

All four records belong to the same domain, `praxis-weiterkommen.ch`. They are not conflicting records; GitHub Pages documents this configuration for custom apex domains.

## 2. Yes, `dig` will return all four IP addresses

Run this on Ubuntu:

```
dig +short A praxis-weiterkommen.ch
```

Expected output (the order can vary):

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

GitHub's documentation uses this same approach to verify the records.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.github.com\&sz=32)

GitHub Docs

For a more detailed answer, including DNS record types and TTLs, run:

```
dig praxis-weiterkommen.ch A +noall +answer
```

You should see four `A` record entries.

One important detail: `dig` shows the records returned by the DNS server you queried. If you have just changed the HOSTFACTORY settings, the output may temporarily show old or incomplete results because of DNS caching. You can also query a public resolver directly:

```
dig @1.1.1.1 +short A praxis-weiterkommen.ch
```

Once all four addresses appear, check that `www` points to your GitHub Pages hostname:

```
dig +short CNAME www.praxis-weiterkommen.ch
```

That should return `YOUR-USERNAME.github.io.` with your actual GitHub username substituted.

praxis-weiterkommen.ch.
Für diesen Hostnamen ist ein DNS-Alias aktiv.
Dieser Eintrag wird automatisch anhand des Ziel-Hostnamens aktualisiert und kann nicht manuell bearbeitet werden.

# 04.11.2026 work on home page
```
TODO: 
- add start button to go to the main index
- change font of title to samye style as the rest (with non seriff font)
- check cookie settings and add stuff user confirmation if required
- check why it is not https by default
- suggest to add images some unused images in the static folder
- keep the not det approved image

In Github I have:
 Custom domain: praxis-weiterkommen.ch
  Enforce HTTPS on

In Hostfactory https://my.hostfactory.ch/ I have following DNS settings:
$TTL  900
@ 900 IN  SOA ns01.hostfactory.ch.  hostmaster.praxis-weiterkommen.ch.  2026110310  7200  7200  1209600 7200
@     NS  ns01.hostfactory.ch.
@     NS  ns02.hostfactory.ch.
www     CNAME @
@     TXT ("v=spf1 a mx include:spf.hostfactory.ch -all")
_dmarc      TXT ("v=DMARC1\; p=quarantine")
@     A 185.199.108.153
@     A 185.199.109.153
@     A 185.199.110.153
@     A 185.199.111.153
@     MX  0 .

At work, something is blocked, probably because only http but not https.

Do I have to create a DNS alias ?
Are there some other checks to do? 

https://praxis-weiterkommen.ch/

https://github.com/ganymede42/praxis-weiterkommen/settings/pages

www CNAME ganymede42.github.io.
```
---------------------------
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ curl -Iv https://praxis-weiterkommen.ch
* Host praxis-weiterkommen.ch:443 was resolved.
* IPv6: (none)
* IPv4: 185.199.110.153, 185.199.111.153, 185.199.108.153, 185.199.109.153
*   Trying 185.199.110.153:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
*   CApath: /etc/ssl/certs
* Recv failure: Connection reset by peer
* TLS connect error: error:00000000:lib(0)::reason(0)
* OpenSSL SSL_connect: Connection reset by peer in connection to praxis-weiterkommen.ch:443 
* closing connection #0
curl: (35) Recv failure: Connection reset by peer
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ curl -4 -Iv https://praxis-weiterkommen.ch
* Host praxis-weiterkommen.ch:443 was resolved.
* IPv6: (none)
* IPv4: 185.199.111.153, 185.199.110.153, 185.199.108.153, 185.199.109.153
*   Trying 185.199.111.153:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
*   CApath: /etc/ssl/certs
* Recv failure: Connection reset by peer
* TLS connect error: error:00000000:lib(0)::reason(0)
* OpenSSL SSL_connect: Connection reset by peer in connection to praxis-weiterkommen.ch:443 
* closing connection #0
curl: (35) Recv failure: Connection reset by peer
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ curl -6 -Iv https://praxis-weiterkommen.ch
* Could not resolve host: praxis-weiterkommen.ch
* Store negative name resolve for praxis-weiterkommen.ch:443
* shutting down connection #0
curl: (6) Could not resolve host: praxis-weiterkommen.ch
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ curl -Iv https://www.praxis-weiterkommen.ch
* Host www.praxis-weiterkommen.ch:443 was resolved.
* IPv6: (none)
* IPv4: 185.199.111.153, 185.199.109.153, 185.199.108.153, 185.199.110.153
*   Trying 185.199.111.153:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
*   CApath: /etc/ssl/certs
* Recv failure: Connection reset by peer
* TLS connect error: error:00000000:lib(0)::reason(0)
* OpenSSL SSL_connect: Connection reset by peer in connection to www.praxis-weiterkommen.ch:443 
* closing connection #0
curl: (35) Recv failure: Connection reset by peer
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ echo "=== DNS ==="
dig +short A praxis-weiterkommen.ch
dig +short AAAA praxis-weiterkommen.ch
dig +short CNAME www.praxis-weiterkommen.ch

echo "=== HTTPS ==="
curl -4 -sSI https://praxis-weiterkommen.ch
curl -6 -sSI https://praxis-weiterkommen.ch

echo "=== HTTP ==="
curl -4 -sSI http://praxis-weiterkommen.ch
=== DNS ===
185.199.110.153
185.199.111.153
185.199.108.153
185.199.109.153
praxis-weiterkommen.ch.
=== HTTPS ===
curl: (35) Recv failure: Connection reset by peer
curl: (6) Could not resolve host: praxis-weiterkommen.ch
=== HTTP ===
HTTP/1.1 503 Service Unavailable
Content-Type: text/html; charset=UTF-8
Content-Length: 9576
Connection: close
P3P: CP="CAO PSA OUR"
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
7. My recommended diagnostic sequence^C
zamofing_t@ganymede:~/Documents/doc-private/praxis-weiterkommen$ openssl s_client \
  -connect praxis-weiterkommen.ch:443 \
  -servername praxis-weiterkommen.ch </dev/null
Connecting to 185.199.110.153
CONNECTED(00000003)
write:errno=104
---
no peer certificate available
---
No client certificate CA names sent
Negotiated TLS1.3 group: <NULL>
---
SSL handshake has read 0 bytes and written 1564 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Protocol: TLSv1.3
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
at work:
https://praxis-weiterkommen.ch/ -> This site can’t be reached
---------------------
Your test results are very useful. They narrow the problem down considerably.

Your DNS configuration is correct. The problem is not an HTTP-versus-HTTPS DNS alias.

The important finding is this:

HTTPS handshake fails

```
TLS handshake (Client Hello)
Recv failure: Connection reset by peer
```

Your computer successfully:

1. Resolves the domain.
2. Finds the correct GitHub Pages IP addresses.
3. Establishes a TCP connection to port 443.
4. Sends a TLS Client Hello.

But the connection is reset before the server sends its certificate.

This means the failure occurs during the TLS connection, before HTTP or your website content is involved.

## 1. What your results tell us

| Test           | Result           | Interpretation                          |
| -------------- | ---------------- | --------------------------------------- |
| DNS A          | Four GitHub IPs  | Correct                                 |
| DNS AAAA       | No records       | Fine; IPv4 is used                      |
| www CNAME      | Apex domain      | Correct                                 |
| HTTPS port 443 | Connection reset | TLS connection interrupted              |
| HTTP port 80   | HTTP 503         | Server or intermediary returns an error |

The `HTTP 503` response is particularly interesting. Its `P3P` header is unusual for GitHub Pages and makes me suspicious of an intermediary, such as a corporate web proxy or filtering system.

My leading suspicion is therefore a network-level restriction or proxy at work.

## 2. Identify whether the response comes from GitHub or your company

Please run:

```
curl -v http://praxis-weiterkommen.ch -o /tmp/praxis-response.html
```

Then inspect the response:

```
head -40 /tmp/praxis-response.html
```

If you see a corporate security message, filtering category, or proxy error, we have probably found the source.

Also check whether a proxy is configured:

```
env | grep -i proxy
```

## 3. Test whether GitHub HTTPS itself works

Run:

```
curl -Iv https://github.com
curl -Iv https://pages.github.com
curl -Iv https://YOUR-GITHUB-USERNAME.github.io
```

Replace the username with your actual GitHub account.

Interpretation:

- All three work, but your custom domain fails: likely domain-specific filtering or custom-domain TLS handling.
- All fail: likely broader GitHub or HTTPS filtering.
- GitHub works, but GitHub Pages fails: investigate filtering of GitHub Pages.

## 4. Compare with another network

This is probably the most decisive test.

Connect your laptop temporarily to your mobile phone's hotspot and run:

```
curl -Iv https://praxis-weiterkommen.ch
```

| Result                                       | Likely cause                                          |
| -------------------------------------------- | ----------------------------------------------------- |
| Works on mobile, fails at work               | Corporate firewall, proxy or DNS security             |
| Fails on both                                | Investigate GitHub Pages configuration or certificate |
| Works on mobile and home, fails only at work | Strong evidence of corporate filtering                |

## 5. Check GitHub's certificate status

In your repository:

Settings → Pages

Look at the custom domain section.

You should see:

- DNS check successful.
- Certificate provisioned.
- Enforce HTTPS enabled.

If the certificate is not yet provisioned, GitHub needs to resolve that before HTTPS can work.

## My recommendation

I would not change your DNS records yet.

Your four A records are correct, your CNAME resolves correctly, and IPv6 is not involved.

I would first establish whether your company's network is resetting the TLS connection.

If the mobile hotspot test works, you can give your IT/network team this precise information:

> Outbound HTTPS connections to `praxis-weiterkommen.ch` (GitHub Pages, IPv4 addresses 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) are reset during the TLS handshake. DNS resolution is successful. Please investigate HTTPS filtering, TLS inspection or firewall policies for this domain.

Send me the results of tests 2 and 3, particularly the HTTP 503 response body. That should help distinguish a corporate web filter from a GitHub Pages configuration problem.

# 05.11.2026 10:30:48
```
done:[16:49, 11/4/2026] Monika Kast Perry: Praxis Weiterkommen mal ist es so und mal ist es Praxis weiterkommen geschrieben. Ich bin für die 2. Variante und müsste in der ganzen Homepage konsistent sein.
done:[16:53, 11/4/2026] Monika Kast Perry: Practice Weiterkommen dieser Mix zwischen Englisch und Deutsch sieht komisch aus
done:[16:54, 11/4/2026] Monika Kast Perry: Psychological practice in Birr (Psychotherapeutic praictice in Birr) Es ist eine psychotherapeutische und keine psychologische Praxis
done:[16:55, 11/4/2026] Monika Kast Perry: dito: Psychologische Praxis in Birr (Psychotherapeutische Praxis in Birr)

rg -g '!_orig/**' -g '!Logbook.md' Psychological .
rg -g '!_orig/**' -g '!Logbook.md' Psychologische .

sed -i 's/Psychologische/Psychotherapeutische/' ./layouts/home.html ./layouts/partials/site-footer.html
```
