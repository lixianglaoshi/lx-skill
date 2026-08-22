# lx-skill

<!-- i18n-source-sha256: 8f7ea09654cb0bb0de19cfc653eec692d2bd0e04475dc18457e54d17f358ecc2 -->

[简体中文](README.md) | [English](README.en.md) | Español | [Deutsch](README.de.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`lx-skill` es una colección en evolución de Agent Skills para la educación con IA, la educación de la nueva era, la educación digital y el crecimiento personal. Resume la experiencia de Li Xiang en educación rural, enseñanza apoyada por IA y comunicación dentro de organizaciones jerárquicas. Funciona con Tencent WorkBuddy, Kimi Code y ZCode; también es compatible con Codex, Claude Code y otros agentes que admiten la especificación abierta Agent Skills.

## Skills incluidos

| Skill | Cuándo utilizarlo |
| --- | --- |
| `lx-education-diagnosis` | Diagnóstico educativo global y revisión de decisiones o incidentes concretos de crianza y enseñanza |
| `lx-parent-learning-environment` | Rutinas de deberes, presión familiar, comparaciones, pantallas, tareas poco claras y dificultad inadecuada |
| `lx-ai-learning-coach` | Aprendizaje guiado con aclaración de objetivos, una pregunta por turno, pistas graduales, práctica y explicación del alumno |
| `lx-institutional-social-coach` | Comunicación ascendente, límites laborales, política de oficina y ansiedad social en instituciones u organizaciones jerárquicas |
| `lx-open-class-ai-diagnosis` | Diagnóstico del valor pedagógico, las evidencias, los riesgos y las mejoras concretas de la IA en una clase abierta |
| `lx-gamified-learning-design` | Convierte mecánicas de juego en mecanismos de aprendizaje para hacer visibles y manipulables conceptos, algoritmos, relaciones espaciales y estrategias |
| `lx-subject-visualization` | Convierte temas o problemas en una página didáctica interactiva de un solo archivo: visualización general, geometría espacial, secciones cónicas y reacciones químicas microscópicas |
| `lx-3d-teaching-animation` | Crea una página didáctica 3D que se puede pausar y explorar para estructuras espaciales, transmisión mecánica, fuerzas y movimiento |

Los skills siguen el idioma del usuario. La lógica se mantiene en una sola versión para evitar diferencias entre traducciones.

## Principios

- Diagnosticar sistemas y conductas observables, no personalidades.
- Proteger la autonomía, la curiosidad, el criterio y el esfuerzo sostenible.
- Usar la IA para preguntar, orientar, simular y dar retroalimentación, no para sustituir automáticamente el pensamiento.
- Reconstruir los hechos antes de emitir un juicio o proponer un experimento.
- Reconocer las diferencias de poder sin abandonar la dignidad, la seguridad ni el cumplimiento de las normas.
- No realizar diagnósticos médicos o psicológicos ni utilizar vergüenza, miedo o etiquetas.

## Ejemplos

```text
Usa $lx-education-diagnosis en el modo de revisión de decisiones educativas.
Hoy grité a mi hijo. Pregunta primero por toda la secuencia y después ayúdame a repararla.
```

```text
Usa $lx-ai-learning-coach para enseñarme SQL mediante práctica guiada.
Haz una sola pregunta central cada vez y no reveles inmediatamente la respuesta final.
```

```text
Usa $lx-institutional-social-coach para preparar una actualización para mi responsable.
Separa hechos, interpretaciones, riesgos formales y acciones controlables, y redacta un guion.
```

```text
Usa $lx-open-class-ai-diagnosis para revisar mi clase abierta. Lee primero mi plan y mis diapositivas y dime si la IA transforma el aprendizaje del alumnado o solo exhibe una herramienta.
```

## Descarga

```bash
git clone https://github.com/lixianglaoshi/lx-skill.git
cd lx-skill
```

Cualquier persona puede consultar y descargar este repositorio público. Nadie puede cambiar el repositorio original sin permiso de escritura; los forks y Pull Requests no modifican el original a menos que el propietario los acepte.

## Instalación en agentes de China

### Kimi Code

```bash
mkdir -p ~/.kimi-code/skills
cp -R skills/lx-* ~/.kimi-code/skills/
```

Kimi Code también examina `~/.agents/skills/`. Inicia una sesión nueva e invoca un skill con `/skill:lx-ai-learning-coach`, o permite que el agente lo seleccione automáticamente.

### ZCode

```bash
mkdir -p ~/.zcode/skills
cp -R skills/lx-* ~/.zcode/skills/
```

Abre `Settings → Skills`, pulsa `Refresh`, comprueba que los skills estén habilitados e invócalos con nombres como `$lx-ai-learning-coach`.

### Tencent WorkBuddy

WorkBuddy importa paquetes locales desde su panel de skills. Empaqueta los ocho skills por separado:

```bash
mkdir -p workbuddy-packages
for d in skills/lx-*; do
  name=$(basename "$d")
  (cd "$d" && zip -r "../../workbuddy-packages/${name}.zip" .)
done
```

En WorkBuddy, selecciona `Add Skill → Upload Skill` y carga los ZIP necesarios desde `workbuddy-packages/`. Revisa las instrucciones, scripts y permisos de cualquier skill de terceros antes de importarlo.

## Instalación en Codex

```bash
mkdir -p ~/.agents/skills
cp -R skills/lx-* ~/.agents/skills/
```

Para un solo proyecto, copia los directorios en `.agents/skills/`. Invocación explícita:

```text
$lx-education-diagnosis
$lx-parent-learning-environment
$lx-ai-learning-coach
$lx-institutional-social-coach
$lx-open-class-ai-diagnosis
$lx-gamified-learning-design
$lx-subject-visualization
$lx-3d-teaching-animation
```

## Instalación en Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/lx-* ~/.claude/skills/
```

Para un solo proyecto, copia los directorios en `.claude/skills/`. Invocación explícita:

```text
/lx-education-diagnosis
/lx-parent-learning-environment
/lx-ai-learning-coach
/lx-institutional-social-coach
/lx-open-class-ai-diagnosis
/lx-gamified-learning-design
/lx-subject-visualization
/lx-3d-teaching-animation
```

## Sincronización de traducciones

El archivo chino `README.md` es la fuente documental. Después de traducir una actualización en los seis README, ejecuta:

```bash
python3 scripts/check_i18n_sync.py --update-markers
python3 scripts/check_i18n_sync.py
```

La comprobación se ejecuta solo de forma manual en local. La acción de GitHub está desactivada, por lo que la sincronización de traducciones ya no genera alertas de GitHub. Consulta [docs/i18n-maintenance.md](docs/i18n-maintenance.md).

## Estructura y seguridad

Cada carpeta en `skills/` puede instalarse de forma independiente e incluye un `SKILL.md` estándar, metadatos opcionales de Codex en `agents/openai.yaml` y referencias de carga progresiva. Consulta la [especificación Agent Skills](https://agentskills.io/specification) y el [plan del proyecto](ROADMAP.md).

Este proyecto ofrece reflexión educativa, acompañamiento del aprendizaje, preparación comunicativa y pequeños experimentos de acción. No sustituye servicios psicológicos, médicos, jurídicos o de emergencia. No envíes a una IA nombres reales, datos escolares o laborales, direcciones, información de contacto, documentos confidenciales ni otros datos personales innecesarios.
