$ErrorActionPreference = 'Stop'
$repository = Split-Path -Parent $PSScriptRoot

$required = @(
    'README.md', 'ROADMAP.md', 'LEARNING_RULES.md', 'PROGRESS.md', 'GLOSSARY.md',
    'CURRICULUM_REVIEW.md', 'MENTOR_RULES.md', 'cross-cutting',
    '00-orientation', '01-programming-foundation', '02-mathematics',
    '03-machine-learning', '04-neural-networks', '05-deep-learning',
    '06-transformers', '07-llm', '08-retrieval-and-rag', '09-agents-and-tools',
    '10-serving-and-mlops', '11-production-ai-systems', '12-capstones',
    '13-ai-systems-graduation', 'templates', 'src', 'tests',
    '00-orientation/concepts', '00-orientation/practice',
    '00-orientation/knowledge-check', '00-orientation/knowledge-check/index.html'
)

$missing = foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $repository $relative))) { $relative }
}
if ($missing) { throw "Missing required paths: $($missing -join ', ')" }

$markdownFiles = Get-ChildItem -LiteralPath $repository -Recurse -Filter '*.md' -File
$requiredHeadings = '## WHAT', '## WHY', '## WHEN', '## WHERE', '## WHO', '## HOW', '## FAILURE', '## VERIFY'
$conceptTemplate = Get-Content -LiteralPath (Join-Path $repository 'templates/CONCEPT_TEMPLATE.md') -Raw
foreach ($heading in $requiredHeadings) {
    if (-not $conceptTemplate.Contains($heading)) { throw "Concept template lacks $heading" }
}

$brokenLinks = [System.Collections.Generic.List[string]]::new()
foreach ($file in $markdownFiles) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)')) {
        $target = $match.Groups[1].Value
        if ($target -match '^(https?:|mailto:)') { continue }
        $decoded = [System.Uri]::UnescapeDataString($target)
        $resolved = Join-Path $file.DirectoryName $decoded
        if (-not (Test-Path -LiteralPath $resolved)) {
            $brokenLinks.Add("$($file.FullName): $target")
        }
    }
}
if ($brokenLinks.Count -gt 0) { throw "Broken relative links:`n$($brokenLinks -join "`n")" }

Write-Output "Structure OK: $($markdownFiles.Count) Markdown files checked; concept template has all required dimensions."
