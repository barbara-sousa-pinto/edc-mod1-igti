resource "aws_glue_catalog_database" "matricula" {
  name = "censo_matricula"
}

resource "aws_glue_crawler" "glue_crawler" {
  database_name = aws_glue_catalog_database.matricula.name
  name = "s3_crawler"
  role = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://datalake-barbara/consumer-zone/censo"
  }

  configuration = <<EOF
{
   "Version": 1.0,
   "Grouping": {
      "TableGroupingPolicy": "CombineCompatibleSchemas" }
}
EOF

  tags = {
    CURSO = "EDC"
  }
}