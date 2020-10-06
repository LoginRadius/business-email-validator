plugins {
    kotlin("jvm") version "1.4.10"
}

group = "com.loginradius"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    jcenter()
}

val spekVersion = "2.0.13"

dependencies {
    implementation(kotlin("stdlib"))
    implementation("com.beust:klaxon:5.0.1")
    testImplementation ("org.spekframework.spek2:spek-dsl-jvm:$spekVersion")
    testRuntimeOnly ("org.spekframework.spek2:spek-runner-junit5:$spekVersion")

    // spek requires kotlin-reflect, can be omitted if already in the classpath
    testRuntimeOnly (kotlin("reflect"))
}

// setup the test task
tasks {
    withType<Test> {
        useJUnitPlatform {
            includeEngines("spek2")
        }
    }
}