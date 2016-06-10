###Content deletion from Nexus

In order to delete content from Nexus, follow these instructions.


#### Prerequisites

* You need an API key for the content service.
* You can't be on the VPN (because it blocks port 9000).
* It's helpful to have some kind of JSON formatter for your browser like [this one for Chrome](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa).
* A [URL encoder](http://meyerweb.com/eric/tools/dencoder/) of some kind. I personally use [the escape-utils Atom package](https://atom.io/packages/escape-utils).

#### Listing content

Before deleting content in production, it's a good idea to make sure you know what you're about to delete. You can list the content IDs that are currently present in Nexus by visiting the `/content/` endpoint:

[https://developer.rackspace.com:9000/content/](https://developer.rackspace.com:9000/content/)

List content IDs that begin with a specific base by providing a URL-encoded `?prefix=` parameter, such as:

[https://developer.rackspace.com:9000/content?prefix=https%3A%2F%2Fgithub.com%2Frackerlabs%2Fdocs-dedicated-vcloud](https://developer.rackspace.com:9000/content?prefix=https%3A%2F%2Fgithub.com%2Frackerlabs%2Fdocs-dedicated-vcloud)

Results are returned 100 at a time. You can paginate (awkwardly) by adding `&pageNumber=2` to the end of the URL. The full documentation is in [the content service README](https://github.com/deconst/content-service#get-contentprefixid_prefixpagenumbernumperpagesize).

#### Deleting content

Delete individual envelopes by using `curl` to issue a `DELETE` request to the content service API, using the URL-encoded content ID:

```bash
export APIKEY="..."

curl -X DELETE -H "Authorization: deconst ${APIKEY}" \
  https://developer.rackspace.com:9000/content/https%3A%2F%2Fgithub.com%2Frackerlabs%2Fdocs-dedicated-vcloud
```

(You can copy and paste the `/content/...` bit from the `url` key in the search results in your browser.)

To bulk delete *all* envelopes beneath a content ID base that you've removed or renamed, specify the `?prefix=true` parameter:

```bash
export APIKEY="..."

curl -X DELETE -H "Authorization: deconst ${APIKEY}" \
  https://developer.rackspace.com:9000/content/https%3A%2F%2Fgithub.com%2Frackerlabs%2Fdocs-dedicated-vcloud?prefix=true
```

The documentation for this endpoint is also in [the content service README](https://github.com/deconst/content-service#delete-contentidprefixtrue).
