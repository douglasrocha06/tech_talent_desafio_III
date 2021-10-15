resource "aws_route53_record" "route_dl" {
  zone_id = "Z00892882FUUMIJ25W8YA" #ID da zona hospedada
  name    = "www.db.tech-talent.cf"
  type    = "A"

  alias {
    name                   = "a2916c142a88747ae8235648f691facd-2b08fe68504e68d6.elb.us-east-1.amazonaws.com" #DNS LoadBalancer
    zone_id                = "Z26RNL4JYFTOTI" #Zona hospedada
    evaluate_target_health = true
  }
}