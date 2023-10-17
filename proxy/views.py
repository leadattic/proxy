from django.http import HttpResponse
import urllib.request

path_map = {
  # add all subdomains and the pprt they should get html from
}

def proxy(request):
  # TODO: add support for other 
  parameters = request.GET.urlencode()

  contents = urllib.request.urlopen("http://localhost:" + get_port_and_page(request) +"?"+parameters).read()

  return HttpResponse(contents)


def get_port_and_page(request):
  subdomain = request.build_absolute_uri().replace("http://", "").replace("https://", "").split(".")[0]
  return path_map.get(subdomain) + request.get_full_path()