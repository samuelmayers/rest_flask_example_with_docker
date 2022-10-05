CREATE TABLE "form"
(
    "id" INTEGER NOT NULL,
    "fullname" VARCHAR(200) NOT NULL,
    "phone" VARCHAR(200) NOT NULL,
    "email" VARCHAR(200) NOT NULL UNIQUE,
    PRIMARY KEY("id")
);
