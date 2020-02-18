# terrasnek

![Python unittest Code Coverage](coverage.svg)

_A Python Client for the [Terraform Cloud / Terraform Enterprise API](https://www.terraform.io/docs/cloud/api/index.html)._


### Using `terrasnek`

For more details on using each endpoint, checkout the [`test`](./test) directory.

```
from terrasnek.api import TFC
import os

TFC_TOKEN = os.getenv("TFC_TOKEN", None)

if __name__ == "__main__":
    api = TFC(TFC_TOKEN)
    api.set_organization("YOUR_ORGANIZATION")
```

#### Contributing to `terrasnek`

Currently the following endpoints are supported:

- [ ] [Account](https://www.terraform.io/docs/cloud/api/account.html)
- [x] [Applies](https://www.terraform.io/docs/cloud/api/applies.html)
- [x] [Configuration Versions](https://www.terraform.io/docs/cloud/api/configuration-versions.html)
- [ ] [Cost Estimates](https://www.terraform.io/docs/cloud/api/cost-estimates.html)
- [ ] [Notification Configurations](terraform.io/docs/cloud/api/notification-configurations.html)
- [x] [OAuth Clients](https://www.terraform.io/docs/cloud/api/oauth-clients.html)
- [x] [OAuth Tokens](https://www.terraform.io/docs/cloud/api/oauth-tokens.html)
- [x] [Organizations](https://www.terraform.io/docs/cloud/api/organizations.html)
- [ ] [Organization Tokens](https://www.terraform.io/docs/cloud/api/organization-tokens.html)
- [x] [Plan Exports](https://www.terraform.io/docs/cloud/api/plan-exports.html)
- [x] [Plans](https://www.terraform.io/docs/cloud/api/plans.html)
- [ ] [Policies](https://www.terraform.io/docs/cloud/api/policies.html)
- [ ] [Policy Checks](https://www.terraform.io/docs/cloud/api/policy-checks.html)
- [ ] [Policy Sets](https://www.terraform.io/docs/cloud/api/policy-sets.html)
- [ ] [Registry Modules](https://www.terraform.io/docs/cloud/api/modules.html)
- [x] [Runs](https://www.terraform.io/docs/cloud/api/run.html)
- [ ] [SSH Keys](https://www.terraform.io/docs/cloud/api/ssh-keys.html)
- [x] [State Versions](https://www.terraform.io/docs/cloud/api/state-versions.html)
- [x] [State Version Outputs](https://www.terraform.io/docs/cloud/api/user-tokens.html)
- [x] [Team Access](https://www.terraform.io/docs/cloud/api/team-access.html)
- [x] [Team Memberships](https://www.terraform.io/docs/cloud/api/team-members.html)
- [x] [Team Tokens](https://www.terraform.io/docs/cloud/api/team-tokens.html)
- [x] [Teams](https://www.terraform.io/docs/cloud/api/teams.html)
- [x] [User Tokens](https://www.terraform.io/docs/cloud/api/user-tokens.html)
- [x] [Users](https://www.terraform.io/docs/cloud/api/users.html)
- [x] [Variables](https://www.terraform.io/docs/cloud/api/variables.html)
- [x] [Workspaces](https://www.terraform.io/docs/cloud/api/workspaces.html)
- [x] [Admin Organizations](https://www.terraform.io/docs/cloud/api/admin/organizations.html)
- [ ] [Admin Runs](https://www.terraform.io/docs/cloud/api/admin/runs.html)
- [ ] [Admin Settings](https://www.terraform.io/docs/cloud/api/admin/settings.html)
- [ ] [Admin Terraform Versions](https://www.terraform.io/docs/cloud/api/admin/terraform-versions.html)
- [x] [Admin Users](https://www.terraform.io/docs/cloud/api/admin/users.html)
- [ ] [Admin Workspaces](https://www.terraform.io/docs/cloud/api/admin/workspaces.html)



### Contributing to `terrasnek`

#### Linting the Code

```
make lint
```

#### Building Test Data

```
cd test/testdata/terraform/
tar -zcvf terrasnek_unittest_config_version.tar.gz src/*
```

#### Run a single unit test
```
python3 -m unittest test/applies_test.py
```

#### Running the Tests with Coverage Info

```
source test/secrets/secrets.sh
make coverage
```

#### Publishing to PyPi

```
make pip-package
make pip-publish
```