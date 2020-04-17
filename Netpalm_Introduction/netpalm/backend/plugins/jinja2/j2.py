from backend.core.confload.confload import config

from jinja2schema import infer, to_json_schema

import os

from jinja2 import Template, Environment, FileSystemLoader

class j2:

    def __init__(self, service=False, **kwargs):
        self.kwarg = kwargs.get('kwargs', False)
        if not service:
            self.jinja_template_dir = config().jinja2_templates
        elif service:
            self.jinja_template_dir = config().jinja2_service_templates
        self.file_loader = FileSystemLoader(self.jinja_template_dir)
        self.env = Environment(loader=self.file_loader)

    def path_hierarchy(self, path):
        try:
            files = []
            fileresult = []
            for r, d, f in os.walk(path):
                for file in f:
                    file.strip(path)
                    files.append(os.path.join(r, file))
            if len(files) > 0:
                for f in files:
                    if '.j2' in f:
                        ftmpfile = f.replace('.j2', '')
                        fileresult.append(ftmpfile.replace(path, ''))
            resultdata = {
                    'status': 'success',
                    'data': {
                        "task_result": {
                            "templates":fileresult
                        }
                    }
            }
            return resultdata
        except Exception as e:
            return str(e)

    def gettemplates(self):
        try:
            res = self.path_hierarchy(self.jinja_template_dir)
            return res
        except Exception as e:
            resultdata = {
                    'status': 'error',
                    'data': str(e)
            }
            return resultdata

    def opentemplate(self,template):
        try:
            with open(template) as f:
                res = f.read()
                return str(res)
        except Exception as e:
            return e

    def gettemplate(self, template):
        try:
            templat = self.jinja_template_dir + template + '.j2'
            res = self.opentemplate(templat)
            try:
                schema = infer(res)
                js_schema = to_json_schema(schema)
            except Exception:
                js_schema = "error reading schema"
            resultdata = {
                    'status': 'success',
                    'data': {
                        "task_result": {
                            "template_schema": js_schema,
                            "template_data": res
                        }
                    }
            }
            return resultdata
        except Exception as e:
            resultdata = {
                    'status': 'error',
                    'data': str(e)
            }
            return resultdata

    def render_j2template(self, template, **kwargs):
        try:
            kwargs = kwargs.get("kwargs", False)
            templat = template + '.j2'
            tmp_template = self.env.get_template(templat)
            output = tmp_template.render(kwargs)
            resultdata = {
                    'status': 'success',
                    'data': {
                        "task_result": {
                            "template": template,
                            "template_render_result": str(output),
                        }
                    }
            }
            return resultdata
        except Exception as e:
            return e

def j2gettemplates(service=False):
    if not service:
        t = j2()
        res = t.gettemplates()
        return res
    else:
        t = j2(service=True)
        res = t.gettemplates()
        return res

def j2gettemplate(tmplate, service=False):
    if not service:
        t = j2()
        res = t.gettemplate(tmplate)
        return res
    else:
        t = j2(service=True)
        res = t.gettemplate(tmplate)
        return res

def render_j2template(templat, service=False, **kwargs):
    if not service:
        t = j2()
        res = t.render_j2template(template=templat, kwargs=kwargs["kwargs"])
        return res
    else:
        t = j2(service=True)
        res = t.render_j2template(template=templat, kwargs=kwargs["kwargs"])
        return res