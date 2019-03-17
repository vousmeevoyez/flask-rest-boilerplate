// This is initialize script that trigger additional database user creation and grant permission for the user
db.createUser(
        {
            user: "flask_db_owner",
            pwd: "some_super_st0ngpassw0rd",
            roles: [
                {
                	"role" : "dbOwner",
                	"db" : "flask_starter"
                }
            ]
        }
);